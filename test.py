


import requests
import pandas as pd 
import json
import datetime
import plotly.express as px 


with open('states.json') as f:
    states_data = json.load(f)

df_state = pd.DataFrame(states_data)
df_state = df_state.explode('states')
#adding states coordinates
df2 = pd.read_csv('states_coordinates.csv')
df2.drop('city', axis=1, inplace=True)
df = df_state.merge(df2, on='states')



def update_cholorpeth_realtime():
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

    consumptions = {}
    eia_api_key = "565ac7c9b7e000e9f3f58590dd7b9ba1"

    #get yesterdays date for the api call and give a time to get less data than desired
    date = (datetime.datetime.now() -datetime.timedelta(days=1)).strftime("%Y%m%d") + 'T24Z'

    for region in df['region'].unique():
        url = 'http://api.eia.gov/series/?api_key=' + eia_api_key + \
            '&series_id=' + f'EBA.{region}-ALL.D.H' +f'&start={date}'

        r = requests.get(url)
        json_data = r.json()
        consumptions[region] = json_data.get('series')[0].get('data')[-1][1]

    
    df['consumption'] = df['region'].map(consumptions)

    title = 'Live Temperatures per state'
    fig_temp = px.choropleth(df,
                    locations="states", locationmode="USA-states",
                    color_continuous_scale="Viridis",
                    #color_continuous_scale="Reds",
                    title=title, hover_data= ["temperature","region"],
                    color="temperature",  scope="usa").update_layout(
            xaxis_showgrid=False,
            yaxis_showgrid=True,
            #autosize=False,
            #width=500,
            #height=500,
            paper_bgcolor="#1a1c23", 
            plot_bgcolor="#1a1c23").update_layout(
                geo=dict(bgcolor= "#1a1c23", 
                lakecolor="#1a1c23",
                landcolor='rgba(51,17,0,0.2)')
                )
                # .add_scattergeo(
                #             locations = df_state["states"], 
                #             locationmode = 'USA-states',
                #             text = df_state["states"], 
                #             mode = "text")

    
    fig_consumption = px.choropleth(df,
                locations="states", locationmode="USA-states",
                color_continuous_scale="Reds",
                #color_continuous_scale="Reds",
                title=title, hover_data= ["consumption","region"],
                color="consumption",  scope="usa").update_layout(
        xaxis_showgrid=False,
        yaxis_showgrid=True,
        #autosize=False,
        #width=500,
        #height=500,
        paper_bgcolor="#1a1c23", 
        plot_bgcolor="#1a1c23").update_layout(
            geo=dict(bgcolor= "#1a1c23", 
            lakecolor="#1a1c23",
            landcolor='rgba(51,17,0,0.2)')
            )
            # .add_scattergeo(
            #             locations = df_state["states"], 
            #             locationmode = 'USA-states',
            #             text = df_state["states"], 
            #             mode = "text")

    return fig_temp, fig_consumption


    #return fig_temp, fig_consumption




