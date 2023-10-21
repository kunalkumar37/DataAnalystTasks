import yfinance as yf
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pymongo import MongoClient


client = MongoClient('localhost', 27017)  
db = client['stock_market']
collection = db['icici_data']


def store_stock_data():
    ticker = 'ICICIBANK.NS'
    data = yf.download(tickers=ticker, period='1d', interval='15m')
    latest_data = data.iloc[-1]
    record = {
        'timestamp': datetime.now(),
        'open': latest_data['Open'],
        'high': latest_data['High'],
        'low': latest_data['Low'],
        'close': latest_data['Close'],
        'volume': latest_data['Volume']
    }
    collection.insert_one(record)
    print("Data stored successfully.")


scheduler = BackgroundScheduler()
scheduler.add_job(store_stock_data, 'cron', hour='11-14', minute='*/15')
scheduler.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()
