from datetime import datetime, tzinfo
from symtable import Symbol
from zoneinfo import ZoneInfo
import requests
import json

data_url = "https://backend.copyfuture.me/binance/leaderboard/get-real-time?period=ALL"

user = 'Molenda'

def api_req():
    response_API = requests.get(data_url)
    return json.loads(response_API.text)

data = api_req()

def get_user_data():
    pos_list = []
    for i in data:
        if i['nickName'] == user:
            pos_list.append(i)    
    return pos_list
        

user_data =  get_user_data()

def parse_user_data(user_data):
    print("Position:" , user_data['symbol'])
    time_in_millis = user_data['createTimeStamp'] / 1000
    
    dt = datetime.fromtimestamp(time_in_millis).strftime('%Y-%m-%d %H:%M:%S.%f')
    print("Entry Time:", dt )
    print("Entry:" , user_data['entryPrice'])
    print("Current Price:",  user_data['markPrice'])
    print("Size:",  user_data['amount'])
    print("PNL:",  user_data['pnl'])
    print("---------------------------------")
    
def print_position(user_data):
    print("positions: \n")
    for pos in user_data:
        print(parse_user_data(pos))
        
print_position(user_data)
