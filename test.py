


# import requests
# import pandas as pd 
# import json
# import datetime
# import plotly.express as px 


import requests
import pandas as pd 
import json
import datetime
import plotly.express as px 


# with open('states.json') as f:
#     states_data = json.load(f)

# df_state = pd.DataFrame(states_data)
# df_state = df_state.explode('states')
# #adding states coordinates
# df2 = pd.read_csv('states_coordinates.csv')
# df2.drop('city', axis=1, inplace=True)
# df = df_state.merge(df2, on='states')

# temperatures = {}
# weather_api_key = '4ede6fba261e0478b6419dbd05bf878a'

# for state in df['states']:
#     latitude = df.loc[df['states'] == state, 'latitude'].iloc[0]
#     longitude = df.loc[df['states'] == state, 'longitude'].iloc[0]

#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={weather_api_key}"
#     r = requests.get(url)
#     json_data = r.json()
#     temperatures[state] = json_data["main"]["temp"]

# df['temperature'] = df['states'].map(temperatures)

# consumptions = {}
# eia_api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"

# #get yesterdays date for the api call and give a time to get less data than desired
# date = (datetime.datetime.now() -datetime.timedelta(days=1)).strftime("%Y%m%d") + 'T24Z'

# for region in df['region'].unique():
#     url = 'http://api.eia.gov/series/?api_key=' + eia_api_key + \
#         '&series_id=' + f'EBA.{region}-ALL.D.H' +f'&start={date}'

#     r = requests.get(url)
#     json_data = r.json()
#     consumptions[region] = json_data.get('series')[0].get('data')[-1][1]


# df['consumption'] = df['region'].map(consumptions)



# max_consumption = df['consumption'].max() 
# max_consumption_state = df.loc[df['consumption']==max_consumption, 'states'].values[0]
# min_consumption = df['consumption'].min() 
# min_consumption_state = df.loc[df['consumption']==max_consumption, 'states'].values[0]


# max_temp = df['temperature'].max() 
# max_temp_state = df.loc[df['temperature']==max_temp, 'states'].values[0]
# min_temp = df['temperature'].max() 
# min_temp_state = df.loc[df['temperature']==min_temp, 'states'].values[0]

# print(max_temp,max_temp_state,min_consumption,min_consumption_state)



"""


# Callback to update Top Bar values
@app.callback(Output("top_bar", "children"), [Input("weather_update", "n_intervals")])

    def update_top_bar(orders):

"""



#put this in the main div
        # where the graphs are:
        #   html.Div(
        #             id="top_bar", className="row div-top-bar", children=get_top_bar()
        #         ),


                                #         #this is for the choropeth
                                #     html.Div(className='eight columns div-user-controls',
                                #         children = [
                                #             html.P('Enter a range for cumulative consumption data or a single end date for single day'),
                                #             dcc.DatePickerRange(
                                #                     id='my-date-picker-single',
                                #                     min_date_allowed=frames['NY'].index.date.min(),
                                #                     max_date_allowed=frames['NY'].index.date.max(),
                                #                     start_date = None,
                                #                     initial_visible_month=frames['NY'].index.date.max(),
                                #                     end_date=frames['NY'].index.date.max(),
                                #                     start_date_placeholder_text='Start Date'
                                #                 ),
                                #              html.Button(
                                #                     'Clear start date',
                                #                     id='button'
                                #                 ),
                                #             dcc.Graph(id='geographic_map',
                                #                 config={'displayModeBar': False},
                                #                 animate=None        
                                #                 )
                                #         ]
                    
                                #   ), 

