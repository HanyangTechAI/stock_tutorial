import enum
import json
import requests


class OrderTypes(enum.Enum):
    BUY = 'buy'
    SELL = 'sell'


class HAIStock:
    def __init__(self, host: str, token: str):
        self.host = host
        self.token = token

    def send_order(self, order_type: OrderTypes, ticker: str, shares: int, price: int) -> int:
        url = f'{self.host}/{order_type.value}'
        body = {
            'ticker': ticker,
            'price': price,
            'share': shares
        }
        body = json.dumps(body)

        resp = requests.post(url, data=body, headers={'token': self.token, 'Content-Type': 'application/json'})
        try:
            return resp.json()
        except:
            raise Exception(resp.text)

    def drop_order(self, order_id: int) -> str:
        url = f'{self.host}/drop_order'
        body = {
            'order_id': order_id
        }
        body = json.dumps(body)

        resp = requests.post(url, data=body, headers={'token': self.token, 'Content-Type': 'application/json'})
        return resp.text

    def account_info(self):
        url = f'{self.host}/account'
        resp = requests.get(url, headers={'token': self.token}) 

        return resp.json()