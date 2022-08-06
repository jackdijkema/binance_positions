#!/usr/bin/env python3
import requests
import json
import threading
from TradingData import TradingData
from api import Api
telegram = "5463256842:AAFQoDtCiERemmXGJmzrskjG1JtJV-UyRSg"

user = 'UNCLEBFM'

def main():    
    api = Api()
    api_resp = api.api_req()
    user_data = api.api_resp_to_doc(api_resp)
    
    td = TradingData(user, user_data)
    
    print(td.get_open_pos())
    td.add_to_doc()
    
if __name__ == "__main__":
    main()
