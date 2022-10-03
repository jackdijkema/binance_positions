#!/usr/bin/env python3
import multiprocessing
import requests
import json
from TradingData import TradingData
from Api import Api

def main():    
    user = input('Fill in Binance username 2 follow: ')
    print("Starting bot on user: ", user)

    td = TradingData(user)
    api = Api()
    try:
        api_proc = multiprocessing.Process(target=api.api_process)
        pos_proc = multiprocessing.Process(target=td.update_positions)
        
        api_proc.start()
        pos_proc.start()
    except:
        print("Error: unable to start process(es)")
        
if __name__ == "__main__":
    main()