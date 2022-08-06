# config.json 생성하기
make_config.py 파일에 자신의 토큰을 넣고 실행시킵니다.

# train model
train 폴더에 있는 train 튜토리얼.ipynb 파일을 열어줍니다.(colab이나 jupyter notebook)
나와있는 튜토리얼을 참고해서 모델을 학습시킵니다. 데이터를 가공하거나 모델을 바꾸면서 원하는 성능을 내는 모델을 만듭니다.

# 주식 거래하기
* main.py *
process()함수 : 예측한 값이 현재 값보다 높으면 매수하고 낮으면 매도합니다.
모델 구현에 따라 process 부분은 달라집니다.
1시간마다 거래가 체결되기 1분 전(xx:x9)에 예측과 주문을 하고 거래 체결 1분 후(xx:x1)에 현재 계좌 상태를 보여줍니다. 
