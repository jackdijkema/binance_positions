#!/usr/bin/env python3
from itertools import count
from operator import pos
import json
import telegram_send
import logging
from datetime import *
import time

class TradingData:
    
    def __init__(self, user):
        self.user = user
        self.curr_time = datetime.utcnow()
         
    def get_array_user_positions(self):
        pos_list = []
        for i in self.user_data:
            if i['nickName'] == self.user:
                pos_list.append(i)
        return pos_list
    
    def update_positions(self):
        logging.info("Position Thread %s: starting")
        while True:
            self.user_data = json.load( open( "data.json" ) )
            print("Updating positions...", "Update Time:", datetime.utcnow())
            self.add_to_doc()
            time.sleep(0.5)
    def add_to_doc(self):
        
        with open("positions.txt", "w") as f:
            curr_time = datetime.utcnow()
            print("---------------------------------", file=f)
            print("User:", self.user,file=f)
            print("Current Time:", curr_time, file=f)
            print("---------------------------------", file=f)
            
            for pos in self.get_array_user_positions():
                if pos['closed'] == False:
                    id = pos['id']
                    sym = pos['symbol']
                    entry_price = pos['entryPrice']
                    current_price =  pos['markPrice']
                    size = pos['amount']
                    pnl = pos['pnl']
                    trade_closed = pos['closed']
                    lev = pos['leverage']                
                    time_in_millis = pos['createTimeStamp']
                    dt = datetime.utcfromtimestamp(time_in_millis / 1000)
                    entry_time = dt
                    
                    if dt > self.curr_time:
                        print("Confirmed:", dt, self.curr_time)
                        
                        telegram_send.send(messages=["NEW POSITION"])
                        message = "TradeID: {}  \n Position: {} \n Entry Time: {} \n BOT Time: {} \n Entry Price: {} \n Current Price: {} \n Size: {} \n PNL: {} \n Leverage: {}".format(
                            id, sym, entry_time, curr_time, entry_price, current_price, size, pnl, lev)

                        telegram_send.send(messages=[message])
                        
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
                            
                        