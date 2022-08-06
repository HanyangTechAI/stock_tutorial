import yfinance
import pandas_datareader as pdr
from datetime import datetime, timedelta, timezone


class Nasdaq:
    def __init__(self):
        # 지금까지의 모든 나스닥 지수(^IXIC)를 가져온다.
        # cf. yahoo finance엔 nasdaq 지수 데이터는 1971년 02월 05일부터 존재한다.
        # cf2. 미국 뉴욕은 UTC-4 이다. (지금은 서머타임 기간)
        now = datetime.now(timezone(timedelta(hours=-4)))
        df = pdr.get_data_yahoo('^IXIC', start='1971-02-05', end=now.strftime('%Y-%m-%d'))
        # High           Low          Open         Close      Volume     Adj Close
        self.df = df[['Open', 'High', 'Low', 'Close']]


if __name__ == '__main__':
    nasdaq = Nasdaq()
    print(nasdaq.df)