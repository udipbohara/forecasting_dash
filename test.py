


import requests
import pandas as pd 
import json
import datetime
import plotly.express as px 


import requests
import pandas as pd 
import json
import datetime
import plotly.express as px 
import numpy as np 

import matplotlib.pyplot as plt
from pmdarima.arima import ARIMA
from datetime import timedelta


pd.plotting.register_matplotlib_converters()

df = pd.read_csv('data/new_york.csv')
df['Date'] = pd.to_datetime(df['Date'])

#converting data to daily usage.
df.index = df.Date
df = df.drop('Date', axis=1)
# resample the dataframe every 1 day (D) and sum ovr each day
df = df.resample('D').sum()
df = df.tz_localize(None)


nyc_weather = pd.read_csv('data/weatherNY.csv')
nyc_weather['DATE'] = pd.to_datetime(nyc_weather['DATE'])
nyc_weather = nyc_weather.set_index('DATE')
nyc_weather.drop(['NAME','STATION'],axis=1,inplace=True)
nyc_weather = nyc_weather['2015-07-01':'2020-08-10']

df = df[:'2020-08-10']


#trying 1 day increments with EXOG. MAYBE BEST CANDIDATE? with fourier terms june to june as 638 and august to august 516

day = 7
real_values = []
predictions = []

df1 = df["2016":"2019"]
nyc_weather = nyc_weather["2016":"2019"]

y = df1.Consumption

exog = pd.DataFrame({'date': y.index})
exog = exog.set_index(pd.PeriodIndex(exog['date'], freq='D'))
exog['is_weekend'] = np.where(exog.index.dayofweek < 5,0,1)



#add weather data

exog['TMIN'] = nyc_weather['TMIN'].values


exog['sin1'] = np.sin(2 * np.pi * exog.index.dayofyear / 638)
exog['cos1'] = np.cos(2 * np.pi * exog.index.dayofyear / 638)


exog['sin2'] = np.sin(4 * np.pi * exog.index.dayofyear /638)
exog['cos2'] = np.cos(4 * np.pi * exog.index.dayofyear /638)


exog['sin3'] = np.sin(2 * np.pi * exog.index.dayofyear / 516)
exog['cos3'] = np.cos(2 * np.pi * exog.index.dayofyear / 516)


exog['sin4'] = np.sin(4 * np.pi * exog.index.dayofyear /516)
exog['cos4'] = np.cos(4 * np.pi * exog.index.dayofyear /516)



exog = exog.drop(columns=['date'])

num_to_update = 0


y_to_train = y.iloc[:(len(y)-100)]    
exog_to_train = exog.iloc[:(len(y)-100)]

dates = []

steps = []

for i in range(5):

    #first iteration train the model
    if i == 0:
        arima_exog_model = ARIMA(order=(3, 0, 1), seasonal_order=(2, 0, 0, 7),exogenous=exog_to_train, error_action='ignore',
                                initialization='approximate_diffuse', suppress_warnings=True).fit(y=y_to_train)  


        preds = arima_exog_model.predict_in_sample(exog_to_train)
        
        #first prediction
        y_to_test = y.iloc[(len(y)-100):(len(y)-100+day)]
        y_exog_to_test = exog.iloc[(len(y)-100):(len(y)-100+day)]
        y_arima_exog_forecast = arima_exog_model.predict(n_periods=day, exogenous=y_exog_to_test)
        
        real_values.append(y_to_test.values)
        predictions.append(y_arima_exog_forecast.tolist())
        
        dates.append(y_to_test.index)
        steps.append(y_to_test.index[-1])
                                                 
        #y_arima_exog_forecast = arima_exog_model.predict(n_periods=2, exogenous=exog_to_test)
    else:
        y_to_update = y.iloc[(len(y)-100+num_to_update):(len(y)-100+num_to_update)+day]
        exog_to_update = exog.iloc[(len(y)-100+num_to_update):(len(y)-100+num_to_update)+day]

        #to test
        to_test = y.iloc[(len(y)-100+num_to_update)+day:(len(y)-100+num_to_update)+(day*2)]
        exog_to_test = exog.iloc[(len(y)-100+num_to_update)+day:(len(y)-100+num_to_update)+(day*2)]
        #update the model

        arima_exog_model.update(y_to_update,exogenous=exog_to_update)
        y_arima_exog_forecast = arima_exog_model.predict(n_periods=day, exogenous=exog_to_test)

        dates.append(to_test.index)
        steps.append(to_test.index[-1])

        predictions.append(y_arima_exog_forecast.tolist())    
        real_values.append(to_test.values)
        
        
        num_to_update += day


predict =  [item for sublist in predictions for item in sublist]
true = [item for sublist in real_values for item in sublist]
dates = [item for sublist in dates for item in sublist]

# predict_increments = [x for x in [i for i in range(len(true))] if x%day == 0]
# predict_increments = [date for date in [i + timedelta(days=i) for i in dates]]
plt.figure(figsize=[50,10])

# plt.plot(dates,true, label='True')
# plt.plot(dates,predict, 'b',label='Predicted')



    #in sample preds

# plt.figure(figsize=[25,7])



#for viz purposes
y_to_train2 = y_to_train[-200:]
plt.plot(y_to_train2,'g',  linewidth=1)
plt.plot(y_to_train2.index,preds[-200:],'r',alpha=.8, linewidth=1, label='Fit')

plt.plot(dates, true, label='True')
plt.plot(dates, predict, 'b',label='Predicted')

for step in steps:
    plt.axvline(step, color='green', linestyle='--', alpha=0.4)




#plt.show()


train_df = y_to_train.to_frame()
train_df['in_sample_preds'] = preds
train_df['date'] = train_df.index
train_df = train_df[-50:]

test_df = pd.DataFrame()
test_df['true'],test_df['pred'] = true,predict
test_df['date'] = test_df.index
test_df.index = dates

fig =px.line(train_df,
            x='date',
            y=['in_sample_preds','Consumption'])



fig2 = px.line(test_df,
            x='date',
            y=['pred','true'])


fig2.show() 