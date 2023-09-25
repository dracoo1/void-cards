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
            _Name = Name[i][0]
            LIST += str(i)+" "+_Name+"\n"
        self.embed = Embed(
            title="List of Cards",
            description=LIST,
            color=0xaa00b6 
        )

#allows for user to search card
class CardSearch:
    def __init__(self, _search):
        try:
            i = int(_search)
            
            self.embed = Embed(
            title="List of Cards",
            description=Name[i][0],
            color=0xaa00b6 
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

