import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("stock_data_july_2025.csv")

# here i will be showing first 10 rows
print(data.head(10))

data.info()

# 2nd step i will clean the data
#removing missing values in place
data.dropna(inplace=True)

# converting 'Data' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

# sorting the Date by descending order
data.sort_values(by='Date', ascending=False, inplace=True)

# 3rd step i will be analyzing trend of stock price
#calculating daily returns
data['Daily_Return'] = data['Close Price'] - data['Close Price'].shift(1)

# this will average return
print("Average Daily Return: ", data['Daily_Return'].mean())

# this is the highest closing price
highest = data['Close Price'].max()
print("Highest Closing Price: ", highest)

# 4th step i will plot a closing price
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close Price'], label='Highest Closing Price', color='blue')
plt.title('Stock Closing Price Over Time - July 2025')
plt.xlabel('Date')
plt.ylabel('Close Price')
#plt.xticks(rotation=45)
plt.legend()
plt.show()

# 5th step it moving average (trend smoothing)
# calculating 7-day moving average
data['MA_7'] = data['Close Price'].rolling(window=7).mean()

# calculating 14-day moving average
data['MA_14'] = data['Close Price'].rolling(window=14).mean()

# plotting closing price with moving averages
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data['Close Price'], label='Closing Price', color='green')
plt.plot(data['Date'], data['MA_7'], label='7-Day MA', color='orange')
plt.plot(data['Date'], data['MA_14'], label='14-Day MA', color='red')

plt.title('Stock Closing Price with Moving Average - July 2025')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()




