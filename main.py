#this is the discord bot that prints whatever is in the string when a user types on of the based takes words.


import discord
import os 
import requests
import json
import random
client = discord.Client()

based_takes_words = [""]

starter_basedtakes = [""]




@client.event
async def on_ready():
  print('We haven logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('$based-takes'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in msg for word in based_takes_words):
    await message.channel.send(random.choice(starter_basedtakes))

client.run(os.getenv('KEY'))




