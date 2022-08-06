import json

file_path = "./config.json"

data = {'server': 'http://mlmi.iptime.org:8000', 'token':'내 토큰 문자열로'}

with open(file_path, 'w') as outfile:
    json.dump(data, outfile)