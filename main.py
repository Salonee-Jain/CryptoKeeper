import discord
import requests
from replit import db
from threading import Timer
from keep_alive import keep_alive
from bs4 import BeautifulSoup as BS
import requests
  
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
  


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))
  

@client.event
async def on_message(message):
  if message.content.startswith("/crypto"):

    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'ebe37ed9-4668-4ea2-8fe8-472328e53828',
    }
    session = Session()

    session.headers.update(headers)


    try:

      response = session.get(url)

      data = json.loads(response.text)

      list1=['Bitcoin','Ethereum','Dogecoin','Polygon','Cardano','XRP']
      for i in range(0,len(data['data'])):

        if(data['data'][i]['name'] in list1):
           await message.channel.send("***"+data['data'][i]['name']+" : $ "+str(round(data['data'][i]['quote']['USD']['price'],2))+"***")
    except:
      print("hello")

keep_alive()

BOT_TOKEN = 'ODk2ODM1MzIwNzQ4ODY3NjU1.YWM4-g.5zbSEBMw4_TySztp3k5S4FXAT5o'
client.run(BOT_TOKEN)