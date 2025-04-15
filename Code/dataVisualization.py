import numpy as np 
import pandas as pd 
import os 
import matplotlib.pyplot as plt
import seaborn as sns 
from datetime import datetime 

output_path = './../output/'

def visualizeAndSaveData(df, company_name):
    data = df[df['company_name'] == company_name]
    df_temp = data.copy()
    save_path = os.path.join(output_path, company_name)
    os.makedirs(save_path, exist_ok=True)

    # Plot the close price
    plt.figure()
    plt.title(f'{company_name} Close Price')
    plt.plot(data['Close'])
    plt.savefig(os.path.join(save_path, 'close_price.png'))
    plt.close()

    # Plot the volume
    plt.figure()
    plt.title(f'{company_name} Volume')
    plt.plot(data['Volume'])
    plt.savefig(os.path.join(save_path, 'volume.png'))
    plt.close()

    # Plot the open, high, and low prices
    plt.figure()
    plt.title(f'{company_name} Open, High, and Low Prices')
    plt.plot(data[['Open', 'High', 'Low']])
    plt.legend(['Open', 'High', 'Low'])
    plt.savefig(os.path.join(save_path, 'open_high_low.png'))
    plt.close()

    # Plot the daily returns
    df_temp['Daily Return'] = df_temp['Close'].pct_change()
    plt.figure()
    plt.title(f'{company_name} Daily Returns')
    plt.plot(df_temp['Daily Return'])
    plt.savefig(os.path.join(save_path, 'daily_returns.png'))
    plt.close()

    # Plot the cumulative returns
    df_temp['Cumulative Return'] = (1 + df_temp['Daily Return']).cumprod()
    plt.figure()
    plt.title(f'{company_name} Cumulative Returns')
    plt.plot(df_temp['Cumulative Return'])
    plt.savefig(os.path.join(save_path, 'cumulative_returns.png'))
    plt.close()

    # Plot the moving averages
    df_temp['20 Day MA'] = df_temp['Close'].rolling(window=20).mean()
    df_temp['50 Day MA'] = df_temp['Close'].rolling(window=50).mean()
    plt.figure()
    plt.title(f'{company_name} 20 and 50 Day Moving Averages')
    plt.plot(df_temp[['Close', '20 Day MA', '50 Day MA']])
    plt.legend(['Close', '20 Day MA', '50 Day MA'])
    plt.savefig(os.path.join(save_path, 'moving_averages.png'))
    plt.close()

    # Plot average daily return values using a histogram
    plt.figure()
    plt.title(f'{company_name} Average Daily Returns')
    plt.hist(df_temp['Daily Return'].dropna(), bins=100)
    plt.savefig(os.path.join(save_path, 'average_daily_returns.png'))
    plt.close()

    # Plot correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure()
    plt.title(f'{company_name} Correlation Matrix')
    sns.heatmap(numeric_df.corr(), annot=True)
    plt.savefig(os.path.join(save_path, 'correlation_matrix.png'))
    plt.close()

    txt_path = os.path.join(save_path, 'data.txt')
    with open(txt_path, 'w') as f:
        f.write(f"Top 5 lines of the data set \n {df.head()} \n")
        f.write(f"Bottom 5 lines of the data set \n {df.tail()} \n")
        f.write(f"Descriptive statistics \n {df.describe()} \n")
        f.write(f"Correlation matrix \n {numeric_df.corr()} \n")
        f.write(f"Data types \n {df.dtypes} \n")
        f.write(f"Null values \n {df.isnull().sum()} \n")
        f.write(f"Data shape \n {df.shape} \n")
        f.write(f"Data columns \n {df.columns} \n")
        f.write(f"Data index \n {df.index} \n")

def visualize_correlation(data):
    save_path = './../output/correlation'
    os.makedirs(save_path, exist_ok=True)

    company_list = data['company_name'].unique()
    closing_df = data.pivot(index='Date', columns='company_name', values='Close')

    tech_rets = closing_df.pct_change().dropna()

    for company in company_list:
        if company != 'AAPL':
            sns.jointplot(x=company, y='AAPL', data=tech_rets, kind='scatter', color='seagreen')
            plt.savefig(os.path.join(save_path, f'{company}_AAPL_correlation.png'))
            plt.close()

    sns.pairplot(tech_rets)
    plt.savefig(os.path.join(save_path, 'pairplot.png'))
    plt.close()

    corr_matrix = tech_rets.corr()

    plt.figure()
    plt.title('Technology Stock Correlation Matrix')
    sns.heatmap(corr_matrix, annot=True)
    plt.savefig(os.path.join(save_path, 'heatmap.png'))
    plt.close()

    rets = tech_rets.dropna()

    plt.figure(figsize=(10, 8))
    plt.scatter(rets.mean(), rets.std(), s=np.pi * 20)
    plt.xlabel('Expected return')
    plt.ylabel('Risk')

    for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
        plt.annotate(label, xy=(x, y), xytext=(50, 50), textcoords='offset points', ha='right', va='bottom', 
                    arrowprops=dict(arrowstyle='-', color='blue', connectionstyle='arc3,rad=-0.3'))
    plt.savefig(os.path.join(save_path, 'risk_return_scatter.png'))
    plt.close()

def visualize_data(df):
    company_list = df['company_name'].unique()

    for company in company_list:
        visualizeAndSaveData(df, company)
    
    visualize_correlation(df)