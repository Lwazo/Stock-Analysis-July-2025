import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="July 2025 Stock Analysis", layout="wide")

st.title("📈 Stock Market Analysis — July 2025")

@st.cache_data
def load_data():
    data = pd.read_csv("stock_data_july_2025.csv")
    data.dropna(inplace=True)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    data.sort_values(by='Date', ascending=True, inplace=True)  # Ascending for easier date filtering
    data['Daily_Return'] = data['Close Price'] - data['Close Price'].shift(1)
    data['MA_7'] = data['Close Price'].rolling(window=7).mean()
    data['MA_14'] = data['Close Price'].rolling(window=14).mean()
    return data

data = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")

# Ticker filter (if available)
if 'Ticker' in data.columns:
    tickers = data['Ticker'].unique()
    selected_tickers = st.sidebar.multiselect("Select ticker(s)", tickers, default=tickers[0])
else:
    selected_tickers = None

# Date range filter
min_date = data['Date'].min()
max_date = data['Date'].max()
start_date, end_date = st.sidebar.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter data by selections
filtered = data.copy()
if selected_tickers:
    filtered = filtered[filtered['Ticker'].isin(selected_tickers)]
filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]

# Sidebar Summary Stats
st.sidebar.header("Summary Statistics")
avg_return = filtered['Daily_Return'].mean()
highest_close = filtered['Close Price'].max()
lowest_close = filtered['Close Price'].min()
total_volume = filtered['Volume Traded'].sum() if 'Volume Traded' in filtered.columns else None

st.sidebar.markdown(f"**Average Daily Return:** {avg_return:.6f}")
st.sidebar.markdown(f"**Highest Close Price:** {highest_close:.2f}")
st.sidebar.markdown(f"**Lowest Close Price:** {lowest_close:.2f}")
if total_volume is not None:
    st.sidebar.markdown(f"**Total Volume Traded:** {total_volume:,}")

# Main content
st.markdown(f"### Displaying data for {', '.join(selected_tickers) if selected_tickers else 'all tickers'} from {start_date} to {end_date}")

st.dataframe(filtered.head(10))

# Layout columns for plots
col1, col2 = st.columns(2)

with col1:
    st.subheader("Closing Price & Moving Averages")
    fig, ax = plt.subplots(figsize=(10, 5))
    for ticker in selected_tickers or filtered['Ticker'].unique():
        df_t = filtered[filtered['Ticker'] == ticker] if 'Ticker' in filtered.columns else filtered
        ax.plot(df_t['Date'], df_t['Close Price'], label=f'{ticker} Close Price')
        ax.plot(df_t['Date'], df_t['MA_7'], linestyle='--', label=f'{ticker} 7-Day MA')
        ax.plot(df_t['Date'], df_t['MA_14'], linestyle=':', label=f'{ticker} 14-Day MA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.set_title('Closing Price with Moving Averages')
    st.pyplot(fig)

with col2:
    st.subheader("Volume Traded Over Time")
    if 'Volume Traded' in filtered.columns:
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        for ticker in selected_tickers or filtered['Ticker'].unique():
            df_t = filtered[filtered['Ticker'] == ticker] if 'Ticker' in filtered.columns else filtered
            ax2.plot(df_t['Date'], df_t['Volume Traded'], label=f'{ticker} Volume')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Volume')
        ax2.legend()
        ax2.set_title('Volume Traded Over Time')
        st.pyplot(fig2)
    else:
        st.info("Volume Traded data not available.")

st.subheader("PE Ratio Trend")
if 'PE Ratio' in filtered.columns:
    fig3, ax3 = plt.subplots(figsize=(12, 4))
    for ticker in selected_tickers or filtered['Ticker'].unique():
        df_t = filtered[filtered['Ticker'] == ticker] if 'Ticker' in filtered.columns else filtered
        ax3.plot(df_t['Date'], df_t['PE Ratio'], label=f'{ticker} PE Ratio')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('PE Ratio')
    ax3.legend()
    ax3.set_title('PE Ratio Trend')
    st.pyplot(fig3)
else:
    st.info("PE Ratio data not available.")

