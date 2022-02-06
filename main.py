import discord
import os
import requests
import json

token = os.environ['bot_token']

client = discord.Client()

def get_quote():
  response = requests.get("https://api.kanye.rest/")
  json_data = json.loads(response.text)
  quote = '"' + json_data['quote'] + '" - Kanye'
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$ye'):
    await message.channel.send(get_quote())

client.run(token)