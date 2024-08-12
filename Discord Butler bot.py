import discord
import os
import wikipedia
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
 print('We have logged in as {0.user}'.format(client))
 try :
  @client.event
  async def on_message(message):
    if message.author == client.user :
      return

   
    if message.content.startswith('%what is') :
      x = message.content.split("%what is ",1)
  
        
      info = wikipedia.summary(x,2)
      await message.channel.send(info)
    
    if message.content.startswith('%who is') :
      y = message.content.split("%who is ",1)
  
        
      info1 = wikipedia.summary(y,2)
      await message.channel.send(info1)

    if message.content.startswith('%why is') :
      z = message.content.split("%why is ",1)
  
        
      info2 = wikipedia.summary(z,2)
      await message.channel.send(info2)

    if message.content.startswith('%where is') :
      a = message.content.split("%where is ",1)
  
        
      info3 = wikipedia.summary(a,2)
      await message.channel.send(info3)
 except Exception :
   pass
     
         


keep_alive()
client.run(os.getenv('TOKEN'))