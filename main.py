import discord


from cardCommands import listAll, CardSearch

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.content.startswith("$help") and len(message.content) <= len("$help"):
        await message.channel.send(f"{message.author.mention}\n$ls - Lists all cards\n$sc * - Search cards")

    if message.content.startswith("$ls") and len(message.content) <= len("$ls"):
        await message.channel.send(f"{message.author.mention}",embed=listAll().embed)

    if message.content.startswith("$sc"):
        search = message.content.split()
        _search = search[-1]
        await message.channel.send(f"{message.author.mention}",file = CardSearch(_search).file, embed=CardSearch(_search).embed)

    if message.content.startswith("$sb") and len(message.content) <= len("$sb"):
        await message.channel.send(f"{message.author.mention}","TEMP SCOREBOARD")
        
    



client.run('MTE1NDU2NzQ3Mjg3NjM3MjAxOA.Gi6FJs.R9ZpXJjALXfpPk_1wKHiRjFarwCIn6b8GKMPG0')