import requests
import json

data_url = "https://backend.copyfuture.me/binance/leaderboard/get-real-time?period=ALL"

def api_req():
    response_API = requests.get(data_url)
    return json.loads(response_API.text)





