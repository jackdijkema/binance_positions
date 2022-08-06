
#!/usr/bin/env python3
from itertools import count
from operator import pos
import requests
import json
import telegram_send
import logging
from datetime import *
import time


class TradingData:
    
    def __init__(self, user):
        self.user = user
        self.user_data = json.load( open( "data.json" ) )
        self.curr_time = datetime.now()
         
    def get_array_user_positions(self):
        pos_list = []
        for i in self.user_data:
            if i['nickName'] == self.user:
                pos_list.append(i)
        return pos_list
    
    def update_positions(self):
        logging.info("Position Thread %s: starting")
        while True:
            print("Updating positions...", "Update Time:", datetime.now())
            if self.add_to_doc() is False:
                print("Waiting new positions...")
                time.sleep(4)
            time.sleep(4)
        
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
                dt = datetime.fromtimestamp(time_in_millis)
                if dt > self.curr_time:
                    telegram_send.send(messages=["NEW POSITION"])
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
                        
                    message = "TradeID: {}  \n Position: {} \n Entry Time: {} \n BOT Time: {} \n Entry Price: {} \n Current Price: {} \n Size: {} \n PNL: {} \n Leverage: {}".format(id, sym, entry_time, self.curr_time, entry_price, current_price, size, pnl, lev)
                    telegram_send.send(messages=[message])

                    
                    
        
    # def listen_new_positions(self):
        
    #     for position in self.get_array_user_positions:
            
    #         id = pos['id']
    #         sym = pos['symbol']
    #         entry_time = dt
    #         entry_price = pos['entryPrice']
    #         current_price =  pos['markPrice']
    #         size = pos['amount']
    #         pnl = pos['pnl']
    #         trade_closed = pos['closed']
    #         lev = pos['leverage']
            
    #         ms = position['createTimeStamp']
    #         dt = datetime.fromtimestamp(ms).strftime('%Y-%m-%d %H:%M:%S.%f')    
    #         if dt > self.curr_time:
    #                 message = "TradeID: {}  \n Position: {} \n Entry Time: {} \n BOT Time: {} \n Entry Price: {} \n Current Price: {} \n Size: {} \n PNL: {} \n Leverage: {}".format(id, sym, entry_time, self.curr_time, entry_price, current_price, size, pnl, lev)
    #                 telegram_send.send(messages=[message])
    #         else:
    #             print("Waiting for new positions...")
    #             self.listen_new_positions()