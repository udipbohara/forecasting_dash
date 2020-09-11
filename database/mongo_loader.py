import pymongo
from pymongo import MongoClient
import requests
import pandas as pd 
import datetime
import json
import datetime

# class Data_loader():
#     def __init__():

# cluster = MongoClient("mongodb+srv://udip:bohara@dashapp.gl7ed.mongodb.net/<dbname>?retryWrites=true&w=majority")

# db = cluster["app_data"]
# collection = db['app_data']

#post = {"_id":0, "name":"udip", "score":5}

#collection.delete_many({})

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
        if collection != None:
            return collection.remove()
        else:
            return self.consumption_collection.delete_many({})

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

            max_date = df['Date'].iloc[0]
           # print(max_date)

            #insert the max date to the database 
            #after that use that value in the next iteration to get the data from it
            self.latest_date_collection.insert_one({
                "_id": region,
                "latest_date": df['Date'].iloc[0]
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
        with open('../states.json') as f:
            states_data = json.load(f)

        for region in [d['region'] for d in states_data]:

            date = self.latest_date_collection.find_one({'_id': region})['latest_date']

            # try to get latest data from it 
            url = 'http://api.eia.gov/series/?api_key=' + self.api_key + \
                  '&series_id=' + f'EBA.{region}-ALL.D.H' +f'&start={date}'

            r = requests.get(url)
            print(url)
            print(r.status_code)

            if r.status_code == 200:
                break
            else:
                print(f'writing new data for time {datetime.datetime.now()}')
                json_data = r.json()
                df = pd.DataFrame(json_data.get('series')[0].get('data'),
                                columns = ['Date','Consumption'])

                max_date = df['Date'].iloc[0]
                print(max_date)
                #insert the max date to the database 
                #after that use that value in the next iteration to get the data from it

                #update latest date
                self.latest_date_collection.replace_one({"_id": region}, df['Date'].iloc[0])

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
                                "consumption_dates": {"$each": consumption_dates},
                                "last_updated" : datetime.datetime.now()           
                                }})
            




    def daily_temperature_data(self):
        pass


    def live_temperature_data(self):
        pass
    

    def get_all(self):
        pass




if __name__ == "__main__":
    #exit()
    database = database_functions()
    #database.delete_data()
    #database.store_consumption_data()
    database.update_consumption_data()





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