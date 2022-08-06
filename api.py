#!/usr/bin/env python3
import requests
import json

import logging
import threading
import time

class Api:
    
    def api_req(self):
        data_url = "https://backend.copyfuture.me/binance/leaderboard/get-real-time?period=ALL"        
        return  requests.get(data_url)
        
    def api_resp_to_doc(self,api_req):
        data = json.loads(api_req.text)
        json.dump( data, open("data.json",'w'))
        return data
    
    def api_process(self):
        logging.info("Api Process %s: starting")
        while True:
            req = self.api_req()
            self.api_resp_to_doc(req)
            print("Updated data.txt", "Status Code:", req.status_code)
            time.sleep(5)