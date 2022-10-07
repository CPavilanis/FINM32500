import math
import os
import random
import re
import sys
import pandas as pd
import numpy as np

def case1(financial_data):
    # Print First 5 rows of MSFT
    print(financial_data.head(5))
    # Print Last 5 rows of MSFT
    print(financial_data.tail(5))
    
def case2(financial_data):
    #Resample to monthly data mean
    financial_data = financial_data.resample('M').mean()
    #Display the first 5 rows
    print(financial_data.head(5))
    
def case3(financial_data):
    # Create a variable daily_close and copy Adj Close from financial_data
    daily_close = financial_data[['Adj Close']].copy()
    daily_returns = daily_close.pct_change()
    # Print first 20 daily returns
    print(daily_returns.head(20))
    
def case4(financial_data):
    # Calculate the cumulative daily returns
    daily_close = financial_data[['Adj Close']].copy()
    daily_returns = daily_close.pct_change()
    # day1 : return1  cumulative reuturn : (1+return1)-1
    # day2 : return2  cumulative reuturn : (1+return1)*(1+return2)-1
    daily_cum_returns = (1 + daily_returns[['Adj Close']]).cumprod() - 1 
    # Print first 20 rows
    print(daily_cum_returns.head(20))
    
def case5(financial_data):
    # Isolate the adjusted closing prices and store it in a variable
    daily_close = financial_data[['Adj Close']].copy()
    # Calculate the moving average for a window of 20
    moving_average = daily_close.rolling(20).mean()
    # Display the last 20 moving average number
    print(moving_average.tail(20))

def case6(financial_data):
    # Calculate the volatility for a period of 100 don't forget to multiply by square root
    daily_close = financial_data[['Adj Close']].copy()
    volatility = daily_close[['Adj Close']].pct_change().rolling(100).std()*10
    # don't forget that you need to use pct_change
    # Print last 20 rows
    print(volatility.tail(20))
