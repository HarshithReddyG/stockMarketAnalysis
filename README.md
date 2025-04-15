# CS5720 - Stock Market Analysis and Predictive Modelling

## Overview
This repository contains the implementation for **CS5720 - Final Project**, focused on **Stock Market Prediction using Deep Learning**. It compares traditional models like **VAR** with advanced models like **LSTM**, and enhances prediction accuracy using **technical indicators (RSI, EMAs)** and **date-based feature engineering**.

## Repository Structure
```
stockMarketAnalysis/
│── Code/
│   ├── main.py
│   ├── dataDownloading.py
│   ├── dataValidation.py
│   ├── dataVisualization.py
│   ├── models.ipynb
│
│── Data/
│   └── stock_data.pkl
│
│── Images/
│   └── *.png (EDA charts, model outputs, predictions)
│
│── Reports/
│   ├── Project Proposal Report.pdf
│   ├── conferenceReport.pdf
│   ├── DemoPresentation.pdf
│   ├── FinalPresentation.pdf
│
├── README.md  # Main ReadMe file
```

## Project Breakdown

### **1. Data Collection & Validation** (`dataDownloading.py`, `dataValidation.py`)
- AAPL stock data (2005–2025) pulled using yfinance.
- Verified date index, handled nulls, and validated formats.

### **2. Exploratory Data Analysis** (`dataVisualization.py`)
- Visualized Close price trends, moving averages, daily/cumulative returns.
- Used correlation heatmaps to understand relationships between price fields.

### **3. Baseline VAR Model** (`models.ipynb`)
- Applied Vector AutoRegression on multivariate series (Open, High, Low, Close, Volume).
- Optimized lag with AIC and evaluated using MSE, RMSE, MAE, R².

### **4. LSTM Model** (`main.py`)
- Univariate LSTM trained on 60-day lookback of AAPL Close prices.
- Used dropout, early stopping, and validated against test set.

### **5. Advanced Feature Engineering & LSTM** (`main.py`)
- Added RSI, EMAF (20), EMAM (100), EMAS (150), and date-based features (Month, Year, DayOfWeek).
- Built a 30-day rolling input window with 11-dimensional feature vectors.
- Achieved improved accuracy with better trend-following during volatile periods.

## Installation & Requirements
Install required packages before running the code:
```sh
pip install yfinance pandas pandas_ta scikit-learn keras matplotlib
```

## Running the Code
To train and evaluate the advanced LSTM model:
```sh
python main.py
```

## Team Members
- Harshith Reddy Gundra  
- Nithin Aaron Kommireddy  
- Varshith Thoutu  
- Bhargav Sai Allam  

## Contact
**Course:** CS5720  
**Institution:** University of Central Missouri  
**GitHub:** https://github.com/HarshithReddyG/stockMarketAnalysis

---
This repository represents a structured, comparative study of statistical and deep learning methods in the context of stock price prediction using AAPL historical data.
