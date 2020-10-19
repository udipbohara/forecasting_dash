

# """populate data"""

# # CREATE SQL DATABASE
# import requests
# import sqlite3
# import json
# import time
# import datetime
# import pandas as pd 
# from sqlalchemy import create_engine


# api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"
# """
# engine = create_engine('test_ny.db', echo=True)
# sqlite_connection = engine.connect()


# key = 'EBA.NY-ALL.D.H'

# api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"

# url = 'http://api.eia.gov/series/?api_key=' + api_key + \
#       '&series_id=' + key

# r = requests.get(url)
# json_data = r.json()


# df_SE = pd.DataFrame(json_data.get('series')[0].get('data'),
#                   columns = ['Date','Consumption'])
# crude = df_SE.copy()
# crude['Year'] = crude.Date.astype(str).str[:4]
# crude['Month'] = crude.Date.astype(str).str[4:6]
# crude['Day'] = crude.Date.astype(str).str[6:8]
# crude['Hour'] = crude.Date.astype(str).str[9:11]
# crude['Date'] = pd.to_datetime(crude[['Year','Month','Day','Hour']])
# crude.drop(['Year','Month','Day','Hour'], axis=1, inplace=True)
# df_SE = crude 

# df_SE = df_SE[df_SE['Consumption'] != 0]
# #df_SE.index = pd.to_datetime(df_SE['Date'])


# sqlite_table = "df_ny"
# df_SE.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

# sqlite_connection.close()
# """



# url = 'http://api.eia.gov/updates/?api_key=' + api_key + \
#       '&category_id=0'

# r = requests.get(url)
# json_data = r.json()
# print(json_data)

# "http://api.eia.gov/updates/?api_key=YOUR_API_KEY_HERE[&category_id=X][&rows=nn]"









