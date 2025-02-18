#importing libraries 
import numpy as np 
import pandas as pd 
import os
import pickle
from dataDownloading import downloadDataFromYahooServer
from dataVisualization import visualize_data

def main():
    pickle_path = "./../Data/stock_data.pkl"
    if os.path.exists(pickle_path):
        print("Pickle file found! Loading downloaded dataset...")
        with open(pickle_path, 'rb') as pkl_file:
            df = pickle.load(pkl_file)
        
    else:
        print("Downloading the data !!!")
        pickle_path = downloadDataFromYahooServer()

    print("Data downloaded successfully!")
    visualize_data(df)


if __name__ == "__main__":
    main()  