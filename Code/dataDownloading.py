import numpy as np 
import pandas as pd 
import os 
import pickle 
import yfinance as yf
from datetime import datetime 

output_path = './../output/'

def downloadDataFromYahooServer():
    # Create output directories
    os.makedirs(output_path, exist_ok=True)
    
    # Redirect output to a file for logging
    output_file = os.path.join(output_path, 'dataDownloading.txt')
    with open(output_file, 'w') as log_file:
        if hasattr(yf, 'pdr_override'):
            yf.pdr_override()
        else: 
            log_file.write("pdr_override() is not available in this version of yfinance\n")
        
        tech_list = ['AAPL', 'MSFT', 'ANET', 'DELL', 'HPQ', 'SMCI', 'HPE']
        end = datetime.now()
        start = datetime(end.year - 8, end.month, end.day)

        company_data = []

        for stock in tech_list:
            try:
                data = yf.download(stock, start=start, end=end)
                data['company_name'] = stock
                log_file.write(f"{stock} daily stock market data for last 5 years\n")
                log_file.write(f"\n{data}\n")
                data.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'company_name']
                company_data.append(data)
            except Exception as e:
                log_file.write(f"Error fetching data for {stock}: {e}\n")

        df = pd.concat(company_data)
        df.reset_index(inplace=True)
        log_file.write(f"Top 5 lines of the data set \n {df.head()} \n")

    pickle_path = './../Data/stock_data.pkl'
    os.makedirs(os.path.dirname(pickle_path), exist_ok=True)
    with open(pickle_path, 'wb') as pkl_file:
        pickle.dump(df, pkl_file)

    return pickle_path