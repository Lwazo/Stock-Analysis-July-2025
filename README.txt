# Stock Market Analysis — July 2025

## Project Overview  
This project analyzes stock market data for July 2025, focusing on daily price trends and moving averages for selected tickers. The goal is to explore stock performance, identify trends, and visualize insights through interactive graphs.

## Dataset  
- Source: [Downloaded from https://www.kaggle.com/datasets/kshitijsaini121/stock-market-prediction-for-july-2025-dataset]  
- Data Range: July 1, 2025 – July 23, 2025  
- Contains columns such as: Date, Ticker, Open Price, Close Price, High Price, Low Price, Volume Traded, Market Cap, PE Ratio, Dividend Yield, EPS, 52 Week High, 52 Week Low, Sector.

## Project Steps  
1. **Data Loading & Inspection:** Loaded the CSV file using Pandas and examined data types and missing values.  
2. **Data Cleaning:** Handled missing or inconsistent data, converted date columns to datetime objects, and sorted the data by date.  
3. **Exploratory Data Analysis:** Calculated daily returns, identified highest and lowest closing prices, and analyzed volume trends.  
4. **Visualization:** Plotted closing prices over time and included 7-day and 14-day moving averages to smooth trends.  
5. **Interactive Dashboard:** Created a Streamlit dashboard to enable interactive exploration of the stock data.

## Key Insights  
•  The 7-day moving average effectively captured short-term price fluctuations, while the 14-day moving average highlighted smoother, longer-term trends.
•  Volume traded peaked mid-month, suggesting increased investor activity that coincided with a price surge.

## Technologies Used  
- Python (Pandas, Matplotlib, Streamlit)  
- VS Code  

## How to Run  
1. Clone this repository.  
2. Install required packages:  
   ```bash  
   pip install pandas matplotlib streamlit  
