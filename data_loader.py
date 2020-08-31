import pandas as pd 
import requests 
import json 


with open('states.json') as f:
    states_data = json.load(f)

def get_data():
    for region in [d['region'] for d in states_data]:
        key = f'EBA.{region}-ALL.D.H'

        print(key)
        api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"


        url = 'http://api.eia.gov/series/?api_key=' + api_key + \
            '&series_id=' + key

        r = requests.get(url)
        json_data = r.json()

        df = pd.DataFrame(json_data.get('series')[0].get('data'),
                        columns = ['Date','Consumption'])

        crude = df.copy()
        crude['Year'] = crude.Date.astype(str).str[:4]
        crude['Month'] = crude.Date.astype(str).str[4:6]
        crude['Day'] = crude.Date.astype(str).str[6:8]
        crude['Hour'] = crude.Date.astype(str).str[9:11]
        crude['Date'] = pd.to_datetime(crude[['Year','Month','Day','Hour']])
        crude.drop(['Year','Month','Day','Hour'], axis=1, inplace=True)
        df = crude 
        #df = df[df['Consumption'] != 0]


        df.to_csv(f'data/{region}.csv', index=False)
#get_data() 




