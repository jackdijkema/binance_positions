import threading
import requests
import json
import telegram_send
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

    # def parse_user_data(self, user_data):
    #     time_in_millis = user_data['createTimeStamp'] / 1000
    #     dt = datetime.fromtimestamp(time_in_millis).strftime('%Y-%m-%d %H:%M:%S.%f')
    #     print("TRADE ID", user_data['id'])
    #     print("Position:" , user_data['symbol'])
    #     print("Entry Time:", dt )
    #     print("Entry Price:" , user_data['entryPrice'])
    #     print("Current Price:",  user_data['markPrice'])
    #     print("Size:", user_data['amount'])
    #     print("PNL:", user_data['pnl'])
    #     print("Trade closed?:", user_data['closed'])
    #     print("leverage:", user_data['leverage'],'x')
    #     print("---------------------------------")
    
    
    # def print_position(self):
    #     counter = 0
    #     print(self.user + " Positions: \n")
    #     for pos in self.user_data:
    #         self.parse_user_data(pos)
        
    def get_open_pos(self):
        open_pos = []
        for i in self.user_data:
            if i['nickName'] == self.user:
                if i['closed'] == False:
                    open_pos.append(i)
        return open_pos
    
    def add_to_doc(self):
        
        with open("positions.txt", "w") as f:
            print("---------------------------------", file=f)
            print("User:", self.user,file=f)
            curr_time = datetime.now()
            print("Current Time:", curr_time, file=f)
            print("---------------------------------", file=f)
            for pos in self.get_array_user_positions():
            
                        time_in_millis = pos['createTimeStamp'] / 1000
                        dt = datetime.fromtimestamp(time_in_millis).strftime('%Y-%m-%d %H:%M:%S.%f')
                        
                        id = pos['id']
                        sym = pos['symbol']
                        entry_time = dt
                        entry_price = pos['entryPrice']
                        current_price =  pos['markPrice']
                        size = pos['amount']
                        pnl = pos['pnl']
                        trade_closed = pos['closed']
                        lev = pos['leverage']
                        
                        print("TRADE ID:", id, file=f)
                        print("Position:" , sym, file=f)
                        print("Entry Time:", dt, file=f )
                        print("Entry Price:" , entry_price, file=f)
                        print("Current Price:",  current_price, file=f)
                        print("Size:", size, file=f)
                        print("PNL:", pnl, file=f)
                        print("Trade closed?:", trade_closed, file=f)
                        print("leverage:", lev,'x', file=f)
                        print("---------------------------------", file=f)
                        
                        # message = "TradeID: {}  \n Position: {} \n Entry Time: {} \n Entry Price: {} \n Current Price: {} \n Size: {} \n PNL: {} \n Leverage: {}".format(id, sym, entry_time, entry_price, current_price, size, pnl, lev)
                        # telegram_send.send(messages=[message])
            
