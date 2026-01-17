import discord
import os 
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()


based_takes_words = ["based"]

starter_basedtakes = [""]


def update_based(based_msg):
  if "base" in db.keys():
    based = db["base"]
    based.append(based_msg)
    db["base"] = based
  else:
    db["base"] = [based_msg]

def delete_based(index):
  based = db["base"]
  if len(based) > index:
    del based[index]
    db["base"] = based


@client.event
async def on_ready():
  print('We haven logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  options = starter_basedtakes
  if "base" in db.keys():
    options.extend(db["base"])
  
  if any(word in msg for word in based_takes_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    based_msg = msg.split("$new ", 1)[1]
    update_based(based_msg)
    await message.channel.send("New based take added.")
    
  if msg.startswith("$del"):
    based = []
    if "base" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_based(index)
      based = db["base"]
    await message.channel.send(based)


keep_alive()

client.run(os.getenv('KEY'))






