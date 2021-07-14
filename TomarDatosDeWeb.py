from bs4 import BeautifulSoup 
import requests
import pandas as pd
import urllib, json
import keyboard
import time

url = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT'
url2 = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT'
while(1):
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())["askPrice"]
	print (data)
	time.sleep(0.01)
	if keyboard.is_pressed('ctrl+e'):
			exit()
