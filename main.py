import discord
from cardCommands import help, listAll, CardSearch, roll

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    
    if message.content.split()[0] == "$help" or message.content.split()[0] == "$h": #help
        await message.channel.send(embed=help().embed)
        
    if message.content.split()[0] == "$ls" or message.content.split()[0] == "$list": #list of all cards
        await message.channel.send(f"{message.author.mention}",embed=listAll().embed)
        
    if message.content.split()[0] == "$sc" or message.content.split()[0] == "$search": #search card
        search = message.content.split()
        _search = search[-1]
        try:
            await message.channel.send(f"{message.author.mention}",file = CardSearch(_search).file, embed=CardSearch(_search).embed)
        except:# if number is invalid it will go through the script a second time just for the error message
            await message.channel.send(f"{message.author.mention}",embed=CardSearch(_search).embed) 
            
    if message.content.split()[0] == "$rl" or message.content.split()[0] == "$roll":
        await message.channel.send(f"{message.author.mention}",embed=roll().embed) 
        
    if message.content.split()[0] == "$sb":
        await message.channel.send(f"{message.author.mention}","TEMP SCOREBOARD")
        




client.run('MTE1NDU2NzQ3Mjg3NjM3MjAxOA.Gi6FJs.R9ZpXJjALXfpPk_1wKHiRjFarwCIn6b8GKMPG0')