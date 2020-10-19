"""
Use this to create functions to retrieve databases in suitable dataframe formats 

Use this to query the database and then return the 


use queries to retrieve desirable data 
"""


"""


import pathlib
import sqlite3
import pandas as pd


DB_FILE = pathlib.Path(__file__).resolve().parent.joinpath("wind-data.db").resolve()


def get_wind_data(start, end):
    Query wind data rows between two ranges
    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT Speed, SpeedError, Direction FROM Wind WHERE rowid > "{start}" AND rowid <= "{end}";'
    df = pd.read_sql_query(statement, con)
    return df


def get_wind_data_by_id(id):
    Query a row from the Wind Table
    :params id: a row id
    :returns: pandas dataframe object


    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT * FROM Wind WHERE rowid = "{id}";'
    df = pd.read_sql_query(statement, con)
    return df

"""


import json
import requests
from datetime import datetime
import pandas as pd 

class my_data:
    pass

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-10"

# temps= []
# r = requests.get(url, headers={"token": "jGaCFmvUlYQggVrUZATZiCdwuCfTFwbi"})
# d = json.loads(r.text)
# #print(d)
# avg_temps = [item for item in d['results'] if item['datatype']=='TMIN']
# temps += [item['value'] for item in avg_temps]
# print(temps)

#initialize dataframe
df_temp = pd.DataFrame()


#initialize lists to store data
dates_temp = []
dates_prcp = []
temps = []
prcp = []

#get all weather data for all the states.







stations = {'CAL':'GHCND:USR0000CACT',
            'CENT':'GHCND:USW00013967',
            'MIDW':'GHCND:USC00470045',
            'MIDA':'GHCND:USW00014895',
            'NE':'GHCND:USC00170409',
            'CAR': 'GHCND:US1NCDV0002',
            'NW':'GHCND:USR0000BLAC',
            'SE':'GHCND:USW00053864',
            'SW':'GHCND:US1AZMR0268',
            'TEN': 'GHCND:USR0000TBIG',
            'TEX' : 'GHCND:USC00410297',
            'NY':'GHCND:USW00014732'}



# function to look for missing values

#pd.date_range(california_weather.index.min(), california_weather.index.max()).difference(california_weather.index)


#for each year from 2015-2019 ...
for year in range(2015, 2021):
    year = str(year)
    print('working on year '+year)
    
    #make the api call
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00014732&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={"token": "jGaCFmvUlYQggVrUZATZiCdwuCfTFwbi"})
    #load the api response as a json
    d = json.loads(r.text)
    #get all items in the response which are average temperature readings
    avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
    #get the date field from all average temperature readings
    dates_temp += [item['date'] for item in avg_temps]
    #get the actual average temperature from all average temperature readings
    temps += [item['value'] for item in avg_temps]


#initialize dataframe
df_temp = pd.DataFrame()

#populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

print(df_temp)
# #initialize lists to store data
# dates_temp = []
# dates_prcp = []
# temps = []
# prcp = []

# #for each year from 2015-2019 ...
# for year in range(2015, 2020):
#     year = str(year)
#     print('working on year '+year)
    
#     #make the api call
#     r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00023129&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
#     #load the api response as a json
#     d = json.loads(r.text)
#     #get all items in the response which are average temperature readings
#     avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
#     #get the date field from all average temperature readings
#     dates_temp += [item['date'] for item in avg_temps]
#     #get the actual average temperature from all average temperature readings
#     temps += [item['value'] for item in avg_temps]


