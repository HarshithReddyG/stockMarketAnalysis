#importing Required Libraries 
import numpy as np 
import pandas as pd 
import os 
import pickle 
import matplotlib.pyplot as plt
import seaborn as sns 

#libraries for yahoo data download
from pandas_datareader.data import DataReader
import yfinance as yf
from pandas_datareader import data as pdr 
#For time stamps 
from datetime import datetime 

output_path = './../output/'

def downloadDataFromYahooServer():
    # Create output directories
    os.makedirs(output_path, exist_ok=True)
    # Redirect output to a file
    output_file = os.path.join(output_path, 'dataDownloading.txt')
    with open(output_file, 'w') as f:
        if hasattr(yf, 'pdr_override'):
            yf.pdr_override()
        else: 
            f.write("pdr_override() is not available in this version of yfinance\n")
        
        # Input the ticker symbol of the company whose data you want to fetch.
        tech_list = ['AAPL', 'ANET', 'DELL', 'HPQ', 'SMCI', 'HPE']

        #setting start and end times for the tech list which we want to fetch 
        end = datetime.now()
        start = datetime(end.year - 5, end.month, end.day)

        # List to hold individual company data
        company_data = []
        
        # Download data for each company and rename columns
        for stock in tech_list:
            data = yf.download(stock, start=start, end=end)
            data['company_name'] = stock
            f.write(f"{stock} daily stock market data for last 5 years\n")
            f.write(f"\n{data}\n")
            # Rename columns to a consistent format
            data.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'company_name']
            company_data.append(data)

        # Concatenate all DataFrames into one
        df = pd.concat(company_data)

        # Reset index to have a clean DataFrame
        df.reset_index(inplace=True)
        f.write(f"Top 5  lines of the data set \n {df.head()} \n")

    # Save the validated dataset to a pickle file
    pickle_path = './../Data/stock_data.pkl'
    os.makedirs(os.path.dirname(pickle_path), exist_ok=True)
    with open(pickle_path, 'wb') as pkl_file:
        pickle.dump(df, pkl_file)

    return pickle_path