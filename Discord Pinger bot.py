import discord
import os
from keep_alive import keep_alive

client = discord.Client()
user1 = input("user1 : ")
key1 = input("Enter key : ")
user2 = input("user2 : ")
key2 = input("Enter key : ")
user3 = input("user3 : ")
key3 = input("Enter key : ")
user4 = input("user4 : ")
key4 = input("Enter key : ")
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user :
      return

    if message.content.startswith('$ping '+user1) :
     x = message.content.split("$ping "+user1,1)
     for i in range(int(x[1])) :
       await message.channel.send(key1)

    if message.content.startswith('$ping '+user2) :
     y = message.content.split("$ping "+user2,1)
     for i in range(int(y[1])) :
       await message.channel.send(key2)

    if message.content.startswith('$ping '+user3) :
     z = message.content.split("$ping "+user3,1)
     for i in range(int(z[1])) :
       await message.channel.send(key3)
    
    if message.content.startswith('$ping '+user4) :
     a = message.content.split("$ping "+user4,1)
     for i in range(int(a[1])) :
       await message.channel.send(key4)
   
keep_alive()
client.run(os.getenv('TOKEN'))