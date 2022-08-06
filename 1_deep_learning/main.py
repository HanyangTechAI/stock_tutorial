from libs.hai_stock import OrderTypes, HAIStock
import yfinance as yf
import pandas_datareader as pdr
from datetime import datetime, timedelta, timezone
import numpy as np

import matplotlib.pyplot as plt
from tensorflow import keras

import pandas as pd

from pandas.plotting import scatter_matrix

from pickle import load
import tensorflow as tf
import json
import schedule
import time

model = keras.models.load_model("train/my_model.h5")
standard_scaler = load(open('train/standard_scaler.pkl', 'rb'))

def buy_stock(stock: HAIStock):
    try:
        num = stock.send_order(OrderTypes.BUY, 'TQQQ', 1000, 10000)
        print(num)
    except:
        print("주문 불가")

def sell_stock(stock: HAIStock):
    try:
        num = stock.send_order(OrderTypes.SELL, 'TQQQ', 1000, 1)
        print(num)
    except:
        print("주문 불가")

def process(stock):
    price = yf.Ticker('TQQQ').history(period='1d')
    now_price = price["Close"].values[0]

    feature = standard_scaler.transform(price[["Open", "High", "Low"]].values)
    feature = feature.reshape(1,1,3)

    predict = model(feature)[0,0].numpy()

    print("예측 : ", predict)
    print("현재 : ", now_price)

    if now_price < predict:
        print("1000개 매수 주문")
        buy_stock(stock)
    elif predict < now_price :
        print("1000개 매도 주문")
        sell_stock(stock)
    
def print_account(stock):
    price = yf.Ticker('TQQQ').history(period='1d')
    now_price = price["Close"].values[0]
    print("현재 : ", now_price) # 거래 체결된 시점은 아님
    print(stock.account_info())

def stock_trading(stock):
    schedule.every().day.at('22:30').do(buy_stock, stock)
    for i in range(22, 29):
        hours = str(i%24).zfill(2)
        min = "09"
        t = hours+":"+min   
        schedule.every().day.at(t).do(process, stock)
        
        min = "29"
        t = hours+":"+min   
        schedule.every().day.at(t).do(process, stock)
        
        min = "49"
        t = hours+":"+min   
        schedule.every().day.at(t).do(process, stock)
        
    schedule.every().day.at('04:49').do(sell_stock, stock)


def print_after_trade(stock):
    schedule.every().day.at('22:41').do(print_account, stock)
    for i in range(23, 29):
        hours = str(i%24).zfill(2)
        min = "01"
        t = hours+":"+min   
        schedule.every().day.at(t).do(print_account, stock)
        min = "31"
        t = hours+":"+min   
        schedule.every().day.at(t).do(print_account, stock)

if __name__ == '__main__':
    with open('config.json', 'rt') as f:
        CONFIG = json.load(f)
    
    stock = HAIStock(CONFIG['server'], CONFIG['token'])

    stock_trading(stock)
    
    print_after_trade(stock)

    while True:
        schedule.run_pending()
        time.sleep(1)
