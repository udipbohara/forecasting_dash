import pymongo
from pymongo import MongoClient
import requests
import pandas as pd 
import datetime
import json


class database_functions(object):
    def __init__(self):
        self.api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"
        self.cluster = MongoClient("mongodb+srv://udip:bohara@dashapp.gl7ed.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.cluster["app_data"]
        #collection to put all the cumulative consumption data
        self.consumption_collection= self.db['consumption_data']
        #collection to put all the temperature data
        self.temperature_collection = self.db['daily_temperature_data']
        #collection to stream the 'live' temperature data for all the states 
        self.live_temp_collection = self.db['live_temperature_data']
        #collection to store the latest dates for temperature and consumption API data 
        self.latest_date_collection = self.db['latest_date_data']
       

    def delete_data(self, collection=None):
        # if collection != None:
        #     return collection.remove()
        # else:
        return self.consumption_collection.delete_many({}), self.latest_date_collection.delete_many({})

    def check_date(self):
        if self.store_consumption_data() > datetime.datetime.now():
            pass 

    
    def store_consumption_data(self):
        with open('../states.json') as f:
            states_data = json.load(f)

        for region in [d['region'] for d in states_data]:
            key = f'EBA.{region}-ALL.D.H'
            url = 'http://api.eia.gov/series/?api_key=' + self.api_key + \
                '&series_id=' + key

            r = requests.get(url)
            json_data = r.json()
            df = pd.DataFrame(json_data.get('series')[0].get('data'),
                            columns = ['Date','Consumption'])


            #max_date = df['Date'].iloc[0]
            max_date = datetime.datetime.strptime(df['Date'].iloc[0][:-1], "%Y%m%dT%H")
    
           # print(max_date)

            #insert the max date to the database 
            #after that use that value in the next iteration to get the data from it
            self.latest_date_collection.insert_one({
                "_id": region,
                "latest_date": max_date
            })

            df['Year'] = df.Date.astype(str).str[:4]
            df['Month'] = df.Date.astype(str).str[4:6]
            df['Day'] = df.Date.astype(str).str[6:8]
            df['Hour'] = df.Date.astype(str).str[9:11]
            df['Date'] = pd.to_datetime(df[['Year','Month','Day','Hour']])

            df.drop(['Year','Month','Day','Hour'], axis=1, inplace=True)
            consumption_dates = df.Date.to_list()
            consumption = df.Consumption.to_list()

            self.consumption_collection.insert_one(
                {"_id": region,
                "region": region,
                "consumption": consumption,
                "consumption_dates": consumption_dates,
                "last_updated": datetime.datetime.now()})


    def update_consumption_data(self):
        # check_update_url = 'http://api.eia.gov/updates/?api_key=565ac7c9b7e000e9f3f58590dd7b9ba1&category_id=2122628&deep=true&rows=1' 
        # r = requests.get(check_update_url)
        # eia_updated_date = datetime.strptime(r.json()['updates'][0]['updated'][:-8], "%Y-%m-%dT%H:%M")

        # current_stored_date = self.latest_date_collection.find_one({'_id': 'CAL'})['latest_date']
        
        with open('../states.json') as f:
            states_data = json.load(f)

        for region in [d['region'] for d in states_data]:
            
            max_date = self.latest_date_collection.find_one({'_id': 'NY'})['latest_date']
            
            to_update_date = (max_date +datetime.timedelta(hours=1)).strftime("%Y%m%dT%HZ") 
            # try to get latest data from it 
            url = 'http://api.eia.gov/series/?api_key=' + self.api_key + \
                '&series_id=' + f'EBA.{region}-ALL.D.H' +f'&start={to_update_date}'
            r = requests.get(url)
            if (r.json().get('series')[0].get('data') != []):                
                # print(url)
                # print(r.status_code)
                print(f'writing new data for {region} at time {datetime.datetime.now()}')
                json_data = r.json()
                df = pd.DataFrame(json_data.get('series')[0].get('data'),
                                columns = ['Date','Consumption'])

                max_date = datetime.datetime.strptime(df['Date'].iloc[0][:-1], "%Y%m%dT%H")
                #insert the max date to the database 
                #after that use that value in the next iteration to get the data from it

                #update latest date
                

                df['Year'] = df.Date.astype(str).str[:4]
                df['Month'] = df.Date.astype(str).str[4:6]
                df['Day'] = df.Date.astype(str).str[6:8]
                df['Hour'] = df.Date.astype(str).str[9:11]
                df['Date'] = pd.to_datetime(df[['Year','Month','Day','Hour']])

                df.drop(['Year','Month','Day','Hour'], axis=1, inplace=True)
                consumption_dates = df.Date.to_list()
                consumption = df.Consumption.to_list()

                self.consumption_collection.update_one(
                    {"_id": region},
                    {"$push": {"consumption": {"$each": consumption},
                                "consumption_dates": {"$each": consumption_dates} 

                                }})
                
                self.consumption_collection.update_one({"_id": region}, { "$set":{"last_updated": datetime.datetime.now()}})
                self.latest_date_collection.replace_one({"_id": region}, {"latest_date": max_date})
            



        #run this every hour 
    def live_temperature_data(self):
        with open('../states.json') as f:
            states_data = json.load(f)

        df_state = pd.DataFrame(states_data)
        df_state = df_state.explode('states')
        #adding states coordinates
        df2 = pd.read_csv('../states_coordinates.csv')
        df2.drop('city', axis=1, inplace=True)
        df_states_main = df_state.merge(df2, on='states')

        df = df_states_main 
        temperatures = {}
        weather_api_key = '4ede6fba261e0478b6419dbd05bf878a'
        for state in df['states']:
            latitude = df.loc[df['states'] == state, 'latitude'].iloc[0]
            longitude = df.loc[df['states'] == state, 'longitude'].iloc[0]
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={weather_api_key}"
            r = requests.get(url)
            json_data = r.json()
            temperatures[state] = json_data["main"]["temp"]

        df['temperature'] = df['states'].map(temperatures)
        states = df.states.to_list()
        temperatures = df.temperature.to_list()

        self.live_temp_collection.update_one({
                "_id": 0},
                {"$set": {"state": states,
                    "temperature": temperatures,
                    "last_updated": datetime.datetime.now() 
                }})



    #need to handle missing data 
    def daily_temperature_data(self):
        pass
    

    def build_temperature_database(self):
        stations = {'CAL':'GHCND:USR0000CACT',
            'CENT':'GHCND:USW00013967', #Oklahoma
            'MIDW':'GHCND:USR0000MMAR', #mississipi 
            'MIDA':'GHCND:USW00014895', #ohio
            'NW':'GHCND:USR0000BLAC', #Utah
            'SE':'GHCND:USW00053864', #Alabama
            'TEN':'GHCND:USR0000TBIG',#Tennessee
            'NY':'GHCND:USW00014732',
            'TEX' : 'GHCND:USW00013962',
            'SW':'GHCND:USR0000AMOS', #Arizona
            'NE':'GHCND:USR0000MMOO', #Maine 
            'CAR': 'GHCND:USC00380184', #SC
            }

        for station, station_key in stations.items():
            dates_temp = []
            dates_prcp = []
            temps = []
            prcp = []
            for year in range(2015, 2021):
                year = str(year)
            #  print('working on year '+year)
                """cant find average temperatures for Carolinas so have to manually look for max and min temperatures and get the average of them"""
                if station == 'CAR':
                    r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&limit=1000&stationid={station_key}&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={"token": "jGaCFmvUlYQggVrUZATZiCdwuCfTFwbi"})
                    d = json.loads(r.text)
                    
                    #print(d['results'])
                    max_temps = [item['value'] for item in d['results'] if item['datatype']=='TMAX']
                    min_temps = [item['value'] for item in d['results'] if item['datatype']=='TMIN']
                    
                    #print(max_temps)
                    dates_temp += [item['date'] for item in [item for item in d['results'] if item['datatype']=='TMAX']] 
                    
                    avg_temps = [(i + j)/2 for i, j in zip(max_temps, min_temps)] 
                
                    temps += avg_temps
                    
                else:
                    r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid={station_key}&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={"token": "jGaCFmvUlYQggVrUZATZiCdwuCfTFwbi"})
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
            df_temp['date'] = [datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
            df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

            
            '''
            there is date with missing values so that needs to be taken care of 
            look for any missing indexes (datetimes) and replace it with the nearest available temperature 
            '''
            df = df_temp.set_index(df_temp['date'])
            idx = pd.date_range(df.index.min(), df.index.max())
            df = df.reindex(idx, method='nearest')
        

            self.temperature_collection.insert_one(
            {"_id": station,
            "region": station,
            "temperature": df.avgTemp.tolist(),
            "dates": df.date.tolist(),
            "latest_date": df.date.max(),
            "last_updated": datetime.datetime.now()})
            
            print(f'{station} ----> success')
   




if __name__ == "__main__":
    #exit()
    database = database_functions()
    #database.live_temperature_data()
    #database.delete_data()
    #database.store_consumption_data()
   # database.update_consumption_data()
    database.build_temperature_database()





#preprocess data


# consumption_collection.insert_one(
#     {"region": "NY",
#      "consumption": consumption,
#      "consumption_dates": consumption_times})

# consumption_times = [item[0] for item in data] 
# consumption = [item[1] for item in data] 
#print(consumption_times)









#make a different collection that has the latest dates "last updated dates"
#that way its not conflicted upon (meaning you are not doing a full date scan)
#make each document for each region 
#use something like collection.update_one({"_id":id, {$"set":{"last_updated"}: latest_date}})

#can do update_many too


# results = collection.find({"name":"udip"})

# for result in results:
#     print(result)


# populate with 
"""



Push data into the array 

db.animal.update(
      { "_id": "100" },
      {
          $push: {
              animalArray: "cat"
          }
      }
  );




//Show most recent order date for each customer.
db.orders.aggregate([
    {$group: {_id: "$customer.number", mostrecent: {$max: "$orderDate"}}
    },
    {$project: {customer: "$_id", mostrecent:1, _id:0}}
])
"""


# collection.insert_one(post)

# collection.insert_many([post1,post2])