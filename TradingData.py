import threading
import requests
import json
from datetime import *

class TradingData:
    
    def __init__(self, user, user_data):
        self.user = user
        self.user_data = user_data
         
    def get_array_user_positions(self):
        pos_list = []
        for i in self.user_data:
            if i['nickName'] == self.user:
                pos_list.append(i)    
        return pos_list

    def parse_user_data(self, user_data):
        time_in_millis = user_data['createTimeStamp'] / 1000
        dt = datetime.fromtimestamp(time_in_millis).strftime('%Y-%m-%d %H:%M:%S.%f')
        
        print("Position:" , user_data['symbol'])
        print("Entry Time:", dt )
        print("Entry Price:" , user_data['entryPrice'])
        print("Current Price:",  user_data['markPrice'])
        print("Size:", user_data['amount'])
        print("PNL:", user_data['pnl'])
        print("Trade closed?:", user_data['closed'])
        print("leverage:", user_data['leverage'],'x')
        print("---------------------------------")
        
    def print_position(self):
        print(self.user + " Positions: \n")
        for pos in self.user_data:
            print(self.parse_user_data(pos))