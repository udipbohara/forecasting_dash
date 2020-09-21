import requests
import datetime
import pandas as pd 
import time 
import numpy as np 



f_date = datetime.datetime.strptime('2020-09-18', '%Y-%m-%d')
l_date = datetime.datetime.utcnow()
delta = l_date - f_date
print(delta.days)


# CENT = 35.3097654,-98.7165585
def get_historical_temps():
    # five_days_ago = datetime.datetime.utcnow() - datetime.timedelta(5)
    # four_days_ago = datetime.datetime.utcnow() - datetime.timedelta(4)
    # unix_time4 = four_days_ago.strftime("%s")
    # unix_time= five_days_ago.strftime("%s")

    weather_api_key = '4ede6fba261e0478b6419dbd05bf878a'
    latitude,longitude = '32.6010112','-86.6807365'

    temperatures = []

    #get weather from five days ago till now.
    for i in range(5,1,-1):
        print(i)
        time = datetime.datetime.utcnow() - datetime.timedelta(i)
        unix_time= time.strftime("%s")
        print(unix_time)
        url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={unix_time}&units=imperial&appid={weather_api_key}"
        r = requests.get(url)
        print(r.json().keys())
        my_list = r.json()["hourly"]
        temp = [d['temp'] for d in my_list]
        temperatures.append(round(np.mean(temp),2))
    
    print(temperatures)


weather_api_key = '4ede6fba261e0478b6419dbd05bf878a'
latitude,longitude = '32.6010112','-86.6807365'
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=hourly,minutely&units=imperial&appid={weather_api_key}"
r = requests.get(url)
#print(r.json().keys())

current_temp = r.json()["current"]["temp"]
print(current_temp)


daily_temp = [d['temp']['day'] for d in r.json()["daily"]]
print(daily_temp)
# # region = "NY"

# # date = "20200910T22Z"
# date = (datetime.datetime.now() -datetime.timedelta(days=1)).strftime("%Y%m%d") + 'T24Z'
# print(date)


# eia_api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"
# # date = (datetime.datetime.now() -datetime.timedelta(days=1)).strftime("%Y%m%d") + 'T24Z'

# # print(date)
# # regio
# region = 'CAL'
# key = f'EBA.{region}-ALL.D.H'


# url = 'http://api.eia.gov/series/?api_key=' + eia_api_key + \
#     '&series_id=' + key + '&start=20200913T01Z' #'&start=20200911T24Z'

# print(url)
# r = requests.get(url)
# json_data = r.json()
# print(json_data.get('series')[0].get('data') == [])

# exit() 

# url = 'http://api.eia.gov/series/?api_key=565ac7c9b7e000e9f3f58590dd7b9ba1&series_id=EBA.CAL-ALL.D.H&start=20200911T24Z'













# #url = "http://api.eia.gov/series/?api_key=565ac7c9b7e000e9f3f58590dd7b9ba1&series_id=EBA.CAL-ALL.D.H&start=20200911T24Z"

# url = 'http://api.eia.gov/updates/?api_key=565ac7c9b7e000e9f3f58590dd7b9ba1&category_id=2122628' #[&deep=true|false][&firstrow=nnnnn][&rows=nn][&out=xml|json]

# url = 'http://api.eia.gov/updates/?api_key=565ac7c9b7e000e9f3f58590dd7b9ba1&category_id=2122628&deep=true'#&rows=5' 
# r = requests.get(url)

# print(r.json())


# #print(r.json()['updates'][0]['updated'])
# date = r.json()['updates'][0]['updated'][:-8]


# updated_date = datetime.strptime(date, "%Y-%m-%dT%H:%M")
# print(updated_date)

# date = "20200910T22"
# date_stored= datetime.strptime(date, "%Y%m%dT%H")


# if updated_date > date_stored:
#     print('yes') 
# else:
#     print('no')
# #print(r.Response)



