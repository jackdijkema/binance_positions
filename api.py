import requests
import json
import threading

class Api:
    
    def api_req(self):
        data_url = "https://backend.copyfuture.me/binance/leaderboard/get-real-time?period=ALL"        
        return requests.get(data_url)
        
    def api_resp_to_doc(self,api_req):
        data = json.loads(api_req.text)
        with open("data.txt","w") as d:
            for i in data:
                d.write(str(i))
        return data
    
    # def updateApi():
    # threading.Timer(5.0, updateApi()).start()
    # return td.api_req()