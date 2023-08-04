import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# Change the tab-title
st.set_page_config(page_title="Stocks", page_icon=":chart_with_upwards_trend:", layout="centered")

st.title("Stock overview")

#------------------------------------------------------------------
# sidebar:
#add_logo("assets/card.jpg", height=300)
#------------------------------------------------------------------

# Make a dropdown menu for the stock tickers
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
ticker_stock = st.selectbox('Stock ticker', ticker_list)

# Set dates to look at:
with st.container():
    col1, col2 = st.columns((1,1))
    with col1:
        start_date = st.date_input("Start date", datetime.date(2019, 1, 1))
    with col2:
        end_date = st.date_input("End date", datetime.date(2021, 1, 31))

# Get data from specified ticker and dates
ticker_data = yf.Ticker(ticker_stock)
ticker_df = ticker_data.history(period='1d', start = start_date, end=end_date)

# Stock name
string_name = ticker_data.info['longName']
st.header(f'Stock Name: {string_name}')

# Ticker dataframe
st.subheader('Data overview')
st.write(ticker_df)

# Bollinger bands
#st.header('Stockprice development ')
#qf = cf.QuantFig(ticker_df, title=' ',legend=False)
#fig = qf.iplot(asFigure=True)
#st.plotly_chart(fig)

# Display linechart of volume
st.subheader("Volume")
st.line_chart(ticker_df.Volume)


#compare multiple stocks