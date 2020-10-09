Interactive Dash app visualizing and forecasting electricity consumption in the US through econometric modeling and FB prophet (LSTM etc).

This app utilizes data from https://www.eia.gov/opendata/ API to pull electricity consumption data.<br>
temperature data from https://noaa.gov to pull electricity data 


Features/Tasks Completed:
- Live clock
- Update of news every 30 minutes
- Historical data for consumption of electricity for each region ( from 2016 ) upto hourly granularity with date sliders.
- Live temperature and electricity consumption data (updated each hour) 
- Forecasting of electricity consumption using SARIMA model (working on others) (daily, weekly, monthly consumptions)
    - The ARIMA model uses exogenous variables (temperature for better prediction)
- Cumulative consumptions using chloropeth maps (get consumption within a timeframe or individual days), polar chart(get consumption for each year for each region based on the seasons)
__current progress:__

![](demo.gif)


Currently working on :
- integrating a mongodb database for backend support to make API calls for Heroku Deployment
- integrating regions for effectively predictions.




