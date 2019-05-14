# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

aapl = pdr.get_data_yahoo("AAPL", start=datetime(
    2012, 1, 1), end=datetime(2016, 1, 1))
aapl.head()
print(aapl.shape)
print(aapl.columns)
print(aapl.describe())
print(aapl.index)
# Select only the last 10 observations of `Close`
ts = aapl['Close'][-10:]
print(ts)


# %%
type(ts)

# %%
# Inspect the first rows of November-December 2006
print(aapl.loc[pd.Timestamp('2012-11-01'):pd.Timestamp('2012-12-31')].head())

# %%
# Inspect the first rows of 2007
print(aapl.loc['2012'].head())

# %%
# Sample 20 rows
sample = aapl.sample(20)

# Print `sample`
print(sample)
# %%
# Resample to monthly level and calculate mean in month
monthly_aapl = aapl.resample('M').mean()

# Print `monthly_aapl`
print(monthly_aapl)


# %%
# Add a column `diff` to `aapl`
aapl['diff'] = aapl.Open - aapl.Close
print(aapl['diff'])

# %%
del(aapl['diff'])
print(aapl.columns)

# %%
# Import Matplotlib's `pyplot` module as `plt`

# Plot the closing prices for `aapl`
aapl['Close'].plot(grid=True)

plt.plot()
# Show the plot
plt.show()

# %%
# Import `numpy` as `np`

# Assign `Adj Close` to `daily_close`
daily_close = aapl[['Adj Close']]
print(daily_close[:100])
# %%

# Daily returns
daily_pct_change = daily_close.pct_change()
print(daily_pct_change[0:100])
# %%
# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily returns
print(daily_pct_change)
# %%
# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)
