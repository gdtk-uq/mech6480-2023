import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

def clean_header(df):
    """ Clean up the header of a dataframe produced from Yahoo Finance."""
    df.columns = df.columns.str.strip().str.lower().str.replace('.', '').str.replace('(', '').str.replace(')', '').str.replace(' ', '_').str.replace('_/_', '/')

def get(tickers, startdate, enddate):
    """ Get stock data from Yahoo Finance:
    Input: tickers (list of strings), startdate (string), enddate (string)
    """
    def data(ticker):
        return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas = map(data, tickers)
    return(pd.concat(datas, keys=tickers, names=['ticker', 'date']))
