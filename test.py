# import pandas as pd 
# import requests 
# import datetime

# import json



# with open('states.json') as f:
#     states_data = json.load(f)

# frames = {}
# for region in [d['region'] for d in states_data]:
#     df = pd.read_csv(f'data/{region}.csv', parse_dates=True)
#     df.index = pd.to_datetime(df['Date'])
#     frames[region] = df 

# app_colors = {"background":"#1a1c23",
#               "text": "#3E3F40",
#               "line": "#C0392B"}



# df = sum(frames['NY'].loc['2020-08-24'].Consumption)


# df_state = pd.DataFrame(states_data)
# df_state = df_state.explode('states')


# frames['NY']= frames['NY'].sort_index()
# print(frames['NY'].loc['2020-06-21':'2020-06-23'])
# exit()
# #put this in callback
# #to get the total consumption chart daily
# values = {}
# for region in df_state['region'].unique():
#       values[region] = sum(frames[region].loc['2020-06-21':'2020-06-23'].Consumption)

# df_state['daily_value'] = df_state['region'].map(values)

# print(df_state)


# # # """

# # # app.layout = html.Div([
# # #     dcc.DatePickerSingle(
# # #         id='my-date-picker-single',
# # #         min_date_allowed=frames['NY'].index.min(),
# # #         max_date_allowed=frames['NY'].index.max()),
# # #         date=str(frames['NY'].index.max()))
# # #     ),
# # #     html.Div(id='output-container-date-picker-single')
# # # ])


# # # @app.callback(
# # #     Output('output-container-date-picker-single', 'children'),
# # #     [Input('my-date-picker-single', 'date')])
# # # def update_output(date):
# # #     string_prefix = 'You have selected: '
# # #     if date is not None:
# # #         date = dt.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
# # #         date_string = date.strftime('%B %d, %Y')
# # #         return string_prefix + date_string


# # # """

# # #select a range or just the end date for a single day data
# # date_selector = dcc.DatePickerRange(
# #         id='my-date-picker-single',
# #         min_date_allowed=frames['NY'].index.date.min(),
# #         max_date_allowed=frames['NY'].index.date.max(),
# #         start_date = None,
# #         end_date=frames['NY'].index.date.max(),
# #         start_date_placeholder_text='Date'
# #     )




# # @app.callback(Output('geographic_map', 'figure'),
# #               [Input('my-date-picker-single', 'start_date'),
# #               Input('my-date-picker-single', 'end_date')]
# #               )
# # def update_geographic_graph(date):

# #     # #to get the total consumption chart daily
# #       if start_date == None:
# #             values = {}
# #             for region in df_state['region'].unique():
# #                   values[region] = sum(frames[region].loc[end_date].Consumption)
# #                   df_state['daily_value'] = df_state['region'].map(values)
# #       else:
# #             values = {}
# #             for region in df_state['region'].unique():
# #                   values[region] = sum(frames[region].loc[start_date:end_date].Consumption)
# #                   df_state['daily_value'] = df_state['region'].map(values)

    
# # # print(df_state)
# #     figa = px.choropleth(df_state,
# #                         locations="states", locationmode="USA-states",
# #                         title=f'Distribution by Region for {date}', color="daily_value", scope="usa").update_layout(
# #                 xaxis_showgrid=False,
# #                 yaxis_showgrid=True,
# #                 #autosize=False,
# #                 #width=500,
# #                 #height=500,
# #                 paper_bgcolor="#1a1c23", 
# #                 plot_bgcolor="#1a1c23").update_layout(
# #                     geo=dict(bgcolor= "#1a1c23", 
# #                     lakecolor="#1a1c23",
# #                     landcolor='rgba(51,17,0,0.2)'))

# #     return figa 




# @app.callback(
#     Output('my-date-picker-single', 'start_date'),
#     [
#         Input('button', 'n_clicks'),
#     ],
#     [
#         State('my-date-picker-single', 'start_date'),
#     ]
# )
# def clear_date(n_clicks, current_selected_date):
#     ''' clears the date when button is clicked'''
#     if (n_clicks is not None) and (n_clicks > 0):
#         # =============================== neither of both following lines work 
#         # return ''
#         return None
#     else:
#         return current_selected_date

