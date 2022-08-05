import requests
import json
import threading

class Api:
    
    def api_req(self):
        data_url = "https://backend.copyfuture.me/binance/leaderboard/get-real-time?period=ALL"        
        return requests.get(data_url)
    
    def api_resp_to_text(self,api_req):
        return json.loads(api_req.text)
    
    # def updateApi():
    # threading.Timer(5.0, updateApi()).start()
    # return td.api_req()