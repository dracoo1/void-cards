import discord
from discord.ext import commands
from discord import Embed

from DBhandler import get_cards
Name, Anime, Power, Type, Rarity, Image, cardCount  = get_cards()

intents = discord.Intents.default()
intents.message_content = True

#Lists all cards
class listAll:
    def __init__(self):
        LIST= """"""
        
        for i in range(cardCount):
            LIST += f"{str(i+1)} {Name[i][0]}  --  {Anime[i][0]}\n"
        self.embed = Embed(
            title="List of Cards",
            description=LIST,
            color=0xaa00b6 
        )

#allows for user to search card
class CardSearch:
    def __init__(self, _search):
        try:
            #card id
            i = int(_search)
            
            #sets file to image
            self.file = discord.File("./cards/"+Image[i-1][0]+".jpg",Image[i-1][0]+".jpg") 
            #lists all card values
            char = (Name[i-1][0]+"\n"+Anime[i-1][0])
            foot= f"Type: {Type[i-1][0]}   Power: {Power[i-1][0]}\n"
            #embed
            self.embed = Embed(
            title="List of Cards",
            #description=desc,
            color=0xaa00b6 
            )
            self.embed.add_field(name="Name", value=char,inline=True)
            self.embed.add_field(name="Rarity", value=Rarity[i-1][0],inline=True)
            self.embed.set_image(url="attachment://"+Image[i-1][0]+".jpg")
            self.embed.set_footer(
            text=foot,
            )
            
        except:
            LIST= """Invalid Number
            Current List: """
            LIST += str(cardCount)
            self.embed = Embed(
                title="List of Cards",
                description=LIST,
                color=0xaa00b6 
            )

