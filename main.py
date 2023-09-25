import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #greetings 
    if message.content.startswith("$test"):
        
        #message.id is user id message.author is username, 
        print (message.id, "+", client.user)
        await message.channel.send("test:)")
        
client.run('MTE1NDU2NzQ3Mjg3NjM3MjAxOA.Gi6FJs.R9ZpXJjALXfpPk_1wKHiRjFarwCIn6b8GKMPG0')