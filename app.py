import pandas as pd 
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import requests 
import datetime
from dash.dependencies import Input, Output, State

#EBA.SE-ALL.D.H
#read states data for map
import json



with open('states.json') as f:
    states_data = json.load(f)


#make a dictionary of all the dataframes
frames = {}
for region in [d['region'] for d in states_data]:
    df = pd.read_csv(f'data/{region}.csv', parse_dates=True)
    df.index = pd.to_datetime(df['Date'])
    frames[region] = df 

app_colors = {"background":"#1a1c23",
              "text": "#3E3F40",
              "line": "#C0392B"}


# Initialise the app
app = dash.Dash(__name__)

# Define the app #this data is template for energy consumption

"""
fig = px.choropleth(italy_last, locations="Country",
                    locationmode=italy_regions,
                    color=np.log(italy_last["TotalPositive"]), 
                    hover_name="Region", hover_data=['TotalPositive'],
                    color_continuous_scale="Sunsetdark", 
                    title='Regions with Positive Cases')
"""

df_state = pd.DataFrame(states_data)
df_state = df_state.explode('states')

#

news_api = 'da8e2e705b914f9f86ed2e9692e66012'
news_api = '46301e508cbb4ecca4096c1f9d407557'

#"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=da8e2e705b914f9f86ed2e9692e66012"


# API Requests for news div

news_requests = requests.get(
    f"http://newsapi.org/v2/everything?q=electricity&apiKey={news_api}"
     #f"http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={news_api}"

)


def update_news():
    json_data = news_requests.json()["articles"]
    news_df = pd.DataFrame(json_data)
    news_df = pd.DataFrame(news_df[["title", "url"]])
    max_rows = 10
    return html.Div(
        children=[
            html.P(className="p-news", children="Headlines: Updates every 30 minutes"),
            html.P(
                className="p-news float-right",
                children="Last update : "
                + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.A(
                                        className="td-link",
                                        children=news_df.iloc[i]["title"],
                                        href=news_df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(news_df), max_rows))
                ],
            ),
        ]
    )

dropdown = dcc.Dropdown(id='tseries-select-dropdown',
                    options=[
                    {'label': 'New York', 'value': 'CAL'},
                    {'label': 'Central', 'value': 'CENT'},
                    {'label': 'Florida', 'value': 'FLA'},
                    {'label': 'Mid-West', 'value': 'MIDW'},
                    {'label': 'Mid-East', 'value': 'MIDA'},
                    {'label': 'North-East', 'value': 'NE'},
                    {'label': 'Carolina', 'value': 'CAR'},
                    {'label': 'North-West', 'value': 'NW'},
                    {'label': 'South-East', 'value': 'SE'},
                    {'label': 'South-West', 'value': 'SW'},
                    {'label': 'Tennessee', 'value': 'TEN'},
                    {'label': 'Texas', 'value': 'TEX'},
                    {'label': 'New-York', 'value': 'NY'}
                ],
                value='NY',
                clearable=False,
                style={'height': '30px', 'width': '200px'}
               # labelStyle={'display': 'inline-block'},
                #style={'align-content':'center'}
            )


dropdown_model = dcc.Dropdown(id='model-select-dropdown',
                    options=[
                    {'label': 'SARIMAX', 'value': 'sarimax'},
                    {'label': 'Prophet', 'value': 'prophet'},
                    {'label': 'LSTM', 'value': 'lstm'},
                ],
                #value='sarimax',
                placeholder="Select a Model",
                #clearable=False,
                style={'height': '30px', 'width': '200px'}
               # labelStyle={'display': 'inline-block'},
                #style={'align-content':'center'}
            )

years_dropdown =  dcc.Dropdown(
                        id='dropdown_polar_chart',
                        options=[{'label':str(k),'value':str(k)} for k in [k for k in range(2015,frames['NY'].index.year.max()+1)  ]   ],
                        value=['2020'],
                        style={'height': '30px', 'width': '400px'},
                        clearable = False,
                        multi=True
                    )  



app.layout = html.Div(children=[

                      html.Div(className='row',  # Define the row element
                               children=[
                                   #interval component for news update every fifteen minutes
                                   #CHANGE THIS
                                   dcc.Interval(id="i_news", interval= 45* 6000, n_intervals=0),
                                   # Interval component for live clock
                                   dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
                                   
                                   dcc.Interval(id='graph_update', interval = 60*6000, n_intervals=0),
                                   
                                   html.Div(className='four columns div-user-controls',
                                        children = [
                                            html.H2('Forecasting - New York Electricity Consumption'),
                                            html.P('''Visualising time series with Plotly - Dash'''),
                                            html.P('Electricity Distribution Region', style={'text-align':'center'}),
                                            html.Div(id="news", children=update_news()),
                                        ]
                    
                                  ), 



                                #thisa is for date and clock and slider and the main graph
                                   # Define the left element
                                    html.Div(className='eight columns div-for-charts bg-grey',
                                            children=[
                                                dcc.Slider(id='slider',
                                                        min=0,
                                                        max=4,
                                                        marks={i: 'Label {}'.format(i) for i in range(5)},
                                                        value=5,
                                                    )  ,
                                                dropdown_model,
                                                dropdown,
                                                html.P(
                                                    id="live_clock",
                                                    className="three-col",
                                                    children='Time : ' + datetime.datetime.now().strftime("%H:%M:%S")
                                                             #style={'text-align':'center'}
                                                        ),

                                                dcc.Graph(id='timeseries',
                                                    config={'displayModeBar': False},
                                                    animate=None,          
                                                    )
                                              
                                  ]),

                                #this is for the choropeth
                                    html.Div(className='eight columns div-user-controls',
                                        children = [
                                            html.P('Enter a range for cumulative consumption data or a single end date for single day'),
                                            dcc.DatePickerRange(
                                                    id='my-date-picker-single',
                                                    min_date_allowed=frames['NY'].index.date.min(),
                                                    max_date_allowed=frames['NY'].index.date.max(),
                                                    start_date = None,
                                                    initial_visible_month=frames['NY'].index.date.max(),
                                                    end_date=frames['NY'].index.date.max(),
                                                    start_date_placeholder_text='Start Date'
                                                ),
                                             html.Button(
                                                    'Clear start date',
                                                    id='button'
                                                ),
                                            dcc.Graph(id='geographic_map',
                                                config={'displayModeBar': False},
                                                animate=None        
                                                )
                                        ]
                    
                                  ), 


                                html.Div(className='fasd-user-controls',
                                        children = [
                                            html.P('Consumption per season'),
                                            html.P('Pick a year or multiple years to see consumption varied by seasons'),
                                            years_dropdown,
                                            dcc.Graph(id='polar_chart',
                                                config={'displayModeBar': False},
                                                animate=None       
                                                )
                                            #html.Div(id="news", children=update_news()),
                                        ]
                    
                                  ), 



                                ]),

                                
]
                      )


@app.callback(Output('geographic_map', 'figure'),
              [Input('my-date-picker-single', 'start_date'),
              Input('my-date-picker-single', 'end_date')])
def update_geographic_graph(start_date,end_date):
# #to get the total consumption chart daily
    if start_date == None:
        title = f'Distribution by Region of {end_date}'
        values = {}
        for region in df_state['region'].unique():
                values[region] = sum(frames[region].loc[end_date].Consumption)
                df_state['consumption_value'] = df_state['region'].map(values)
    else:
        title = f'Distribution by Region from {start_date} to {end_date}'
        values = {}
        for region in df_state['region'].unique():
                values[region] = sum(frames[region].sort_index().loc[start_date:end_date].Consumption)
                df_state['consumption_value'] = df_state['region'].map(values)

    
# print(df_state)
    figa = px.choropleth(df_state,
                        locations="states", locationmode="USA-states",
                        #color_continuous_scale="Reds",
                        title=title, hover_data= ["consumption_value","region"],
                        color="consumption_value",  scope="usa").update_layout(
                xaxis_showgrid=False,
                yaxis_showgrid=True,
                #autosize=False,
                #width=500,
                #height=500,
                paper_bgcolor="#1a1c23", 
                plot_bgcolor="#1a1c23").update_layout(
                    geo=dict(bgcolor= "#1a1c23", 
                    lakecolor="#1a1c23",
                    landcolor='rgba(51,17,0,0.2)'))

    return figa 

#clear start date 
@app.callback(
    Output('my-date-picker-single', 'start_date'),
    [
        Input('button', 'n_clicks'),
    ],
    [
        State('my-date-picker-single', 'start_date'),
    ]
)
def clear_date(n_clicks, current_selected_date):
    ''' clears the date when button is clicked'''
    if (n_clicks is not None) and (n_clicks > 0):
        # =============================== neither of both following lines work 
        # return ''
        return None
    else:
        return current_selected_date



@app.callback(Output('timeseries', 'figure'),
              [Input('tseries-select-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    temp_df = frames[selected_dropdown_value]
    fig=px.line(temp_df,
            x='Date',
            y='Consumption',
            title='Daily Consumption'
            ).update_layout(
            xaxis_showgrid=False,
            yaxis_showgrid=True,
            #autosize=False,
            #width=500,
            #height=500,
            paper_bgcolor="#1a1c23", 
            plot_bgcolor="#1a1c23",
            yaxis=dict(
                titlefont=dict(size=10),
                    ),
            xaxis =dict(
                titlefont=dict(size=10),
                color="#3E3F40"
                    )
                        ).update_traces(line_color='#C0392B'
                        ).update_xaxes(
                            rangeslider_visible=True,
                            rangeselector=dict(
                            buttons=list([
                                #dict(count=1, label="1h", step="hour", stepmode="backward"),
                                dict(count=1, label="1d", step="day", stepmode="backward"),
                                dict(count=7, label="1w", step="day", stepmode="backward"),
                                dict(count=1, label="1m", step="month", stepmode="backward"),
                                dict(count=6, label="6m", step="month", stepmode="backward"),
                                dict(count=1, label="YTD", step="year", stepmode="todate"),
                                dict(count=1, label="1y", step="year", stepmode="backward"),
                                dict(step="all")
                    ])
                )
            )
    return fig 

#update polar chart
@app.callback(Output('polar_chart', 'figure'),
              [Input('dropdown_polar_chart', 'value')])
def update_polar_chart(years):
    seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'fall': [9, 10, 11]
}
    consumption_dict = {}
    for region in df_state['region'].unique():
        df = frames[region]
        consumption_dict[region] = {}
        consumption_dict[region]['summer'] = sum(df[(df.index.year.isin(years)) & (df.index.month.isin(seasons['winter']))].Consumption)
        consumption_dict[region]['spring'] = sum(df[(df.index.year.isin(years)) & (df.index.month.isin(seasons['spring']))].Consumption)
        consumption_dict[region]['fall'] = sum(df[(df.index.year.isin(years)) & (df.index.month.isin(seasons['summer']))].Consumption)
        consumption_dict[region]['winter'] = sum(df[(df.index.year.isin(years)) & (df.index.month.isin(seasons['fall']))].Consumption)

    df = pd.DataFrame([(k,k1,v1) for k,v in consumption_dict.items() for k1,v1 in v.items()], columns = ['region','season','consumption'])
    
    fig = px.bar_polar(df, r="consumption", theta="region", color="season", template="plotly_dark",
                 color_discrete_sequence= ['#ffffb2','#fecc5c','#fd8d3c','#e31a1c']).update_layout(
            xaxis_showgrid=False,
            yaxis_showgrid=True,
            #autosize=False,
            #width=500,
            #height=500,
            paper_bgcolor=app_colors['background']).update_polars(bgcolor=app_colors['background'])
    return fig


# Callback to update news
@app.callback(Output("news", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_news()


# Callback to update live clock
@app.callback(Output("live_clock", "children"), [Input("interval", "n_intervals")])
def update_time(n):
    return datetime.datetime.now().strftime("%H:%M:%S")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


