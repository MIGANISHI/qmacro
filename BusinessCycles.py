import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas_datareader as pdr
import numpy as np

# set the start and end dates for the data
start_date = '2004-04-01'
end_date = '2023-07-01'

# download the data from FRED using pandas_datareader
japan_gdp = web.DataReader('JPNRGDPEXP', 'fred', start_date, end_date)
india_gdp = web.DataReader('NGDPRNSAXDCINQ', 'fred', start_date, end_date)
log_japan_gdp = np.log(japan_gdp)
log_india_gdp = np.log(india_gdp)

# calculate the quarterly percent change in real GDP
japan_gdp_pct_change = japan_gdp.pct_change(4)
india_gdp_pct_change = india_gdp.pct_change(4)

# apply a Hodrick-Prescott filter to the data to extract the cyclical component
cycle = sm.tsa.filters.hpfilter(log_japan_gdp)
cycle = sm.tsa.filters.hpfilter(log_india_gdp)

# Plot the original time series data
plt.plot(log_japan_gdp, label="Japan GDP (in log)")
plt.plot(log_india_gdp, label="India GDP (in log)")

# Add a legend and show the plot
plt.legend()
plt.show()

cycle_mean = cycle.mean()
cycle_std = cycle.std()

print("Cycle mean:", cycle_mean)
print("Cycle standard deviation:", cycle_std)
