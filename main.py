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
    if message.content.startswith("$help"):
        await message.channel.send("temp help menu")

    if message.content.startswith("$lc"):
        await message.channel.send(embed=listAll().embed)

    if message.content.startswith("$sc"):
        search = message.content.split()
        _search = search[-1]
        await message.channel.send(embed=CardSearch(_search).embed)

    if message.content.startswith("$sb"):
        await message.channel.send("TEMP SCOREBOARD")
        
    



client.run('MTE1NDU2NzQ3Mjg3NjM3MjAxOA.Gi6FJs.R9ZpXJjALXfpPk_1wKHiRjFarwCIn6b8GKMPG0')