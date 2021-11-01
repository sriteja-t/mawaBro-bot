import os
import discord
import requests
import random
client = discord.Client()

@client.event
async def on_ready():
 print('back to life!')

@client.event
# server specific cmds
async def on_message(message):
  gif = ["https://"]
  for i in range(len(gif)):
   if gif[i] in message.content and str(message.channel) == "area-51-zoo":
     await message.channel.send('approved')
   elif str(message.channel) == "area-51-zoo" and message.content != "":
     await message.channel.purge(limit=1)
  
 # delete all messages where deleting capability is limited to 100 messages    
  if str(message.channel) == "images"  and message.content == "DELETE ALL":
    await message.channel.purge(limit=100)

 # 1 for panda images   
  if message.content == "get panda":
   response = requests.get('https://some-random-api.ml/animal/panda')
   data = response.json()
   myEmbed = discord.Embed(title = "*Pandaa*",colour= discord.Color.random())
   myEmbed.set_image(url=data['image'])
   await message.channel.send(embed = myEmbed)

 # 2 for wink images
  if message.content == "bored wink":
   response = requests.get('https://some-random-api.ml/animu/wink')
   data = response.json()
   myEmbed = discord.Embed(title = "*wink wink*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['link'])
   await message.channel.send(embed = myEmbed)  

 # 3 for bird images
  if message.content == "get bird":
   response = requests.get('https://some-random-api.ml/img/birb')
   data = response.json()
   myEmbed = discord.Embed(title = "*toTheMoon*", description = 'flap flap', colour= discord.Color.random())
   myEmbed.set_image(url=data['link'])
   await message.channel.send(embed = myEmbed)  
  
  # 4 for dog images
  if message.content == "get dog":
   response = requests.get('https://some-random-api.ml/animal/dog')
   data = response.json()
   myEmbed = discord.Embed(title = "*Boww!*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['image'])
   await message.channel.send(embed = myEmbed)  

 # 5 for fox images 
  if message.content == "get fox":
   response = requests.get('https://randomfox.ca/floof/')
   data = response.json()
   myEmbed = discord.Embed(title = "*fox served*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['image'])
   await message.channel.send(embed = myEmbed) 

  # 6 for cat images  
  if message.content == "get cat":
   response = requests.get('http://aws.random.cat/meow')
   data = response.json()
   myEmbed = discord.Embed(title = "*meoww*", description = 'cutiee', colour= discord.Color.blurple())
   myEmbed.set_image(url=data['file'])
   await message.channel.send(embed = myEmbed) 

 # 7 for rat images
  if message.content == "get rat":
   response = requests.get('https://rat-api-image.herokuapp.com/rat/get')
   data = response.json()
   myEmbed = discord.Embed(title = "*no cat can catch me*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['img'])
   await message.channel.send(embed = myEmbed) 

 # 8 for shiba images
  if message.content == "get shiba":
   response = requests.get('http://shibe.online/api/shibes')
   data = response.json()
   myEmbed = discord.Embed(title = "*Shibaaa*" , colour= discord.Color.random())
   myEmbed.set_image(url=data[0])
   await message.channel.send(embed = myEmbed) 

 # 9 for bunny images
  if message.content == "get bunny":
   response = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif,png')
   data = response.json()
   myEmbed = discord.Embed(title = "*Carrots plzz*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['media']['gif'])
   await message.channel.send(embed = myEmbed)      
   

  # bored 
  if message.content == "bored cat":
    response = requests.get('https://some-random-api.ml/facts/cat')
    data = response.json()
    await message.channel.send(data['fact']) 
  if message.content == "bored panda":
    response = requests.get('https://some-random-api.ml/facts/panda')
    data = response.json()
    await message.channel.send(data['fact'])
  if message.content == "bored dog":
    response = requests.get('https://some-random-api.ml/facts/dog')
    data = response.json()
    await message.channel.send(data['fact'])
  if message.content == "bored fox":
    response = requests.get('https://some-random-api.ml/facts/fox')
    data = response.json()
    await message.channel.send(data['fact']) 
  if message.content == "bored bird":
    response = requests.get('https://some-random-api.ml/facts/bird')
    data = response.json()
    await message.channel.send(data['fact'])   
  if message.content == "bored joke":
    response = requests.get('https://some-random-api.ml/joke')
    data = response.json()
    await message.channel.send(data['joke'])   


  # random cmds
  list = ['get fox','get shiba','get bunny', 'get cat','get rat','get panda','get dog','get bird','bored panda','bored cat','bored dog','bored bird','bored wink']
  value = random.choice(list)
  if message.content == "BORED":
   await message.channel.send(value)   

  return

client.run(os.getenv('api_token'))

