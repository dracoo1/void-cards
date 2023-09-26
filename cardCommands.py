import discord
from discord.ext import commands
from discord import Embed
import random
import time
import numpy

from DBhandler import get_cards
Id, CName, Anime, Power, Type, Rarity, Image, cardCount  = get_cards()
from DBhandler import get_user
UserID, Name, G, Shards, Cards, playerCount = get_user()
from DBhandler import get_rarity
CCount, Common = get_rarity()

intents = discord.Intents.default()
intents.message_content = True

#help menu
class help:
    def __init__(self):
        HTEXT=f"$ls/$list - lists all cards\n$sc/$search (cardId) - search for card\n$rl/$roll roll for card"
        
        self.embed = Embed(
            title="Help",
            description=HTEXT,
            color=0xaa00b6 
        )

#Lists all cards
class listAll:
    def __init__(self):
        LIST= """"""
        
        for i in range(cardCount):
            LIST += f"{str(i+1)} {CName[i][0]}  --  {Anime[i][0]}\n"
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
            
            #prevents users from entering an invalid number
            if i <= 0:
                i = None
            
            #sets file to image
            self.file = discord.File("./cards/"+Image[i-1][0]+".jpg",Image[i-1][0]+".jpg") 
            #lists all card values
            char = (CName[i-1][0]+"\n"+Anime[i-1][0])
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
            print("error")
            LIST= """Invalid Number
            Current List: """
            LIST += str(cardCount)
            self.embed = Embed(
                title="List of Cards",
                description=LIST,
                color=0xaa00b6 
            )

class roll:
    def __init__(self):
        _roll = random.random()


# Define the match statement
        match _roll:
            case _ if 0 <= _roll < 0.5:##0 - 0.5
                ran = random.randint(0,CCount[0][0]-1)
                e = (f"{Common[ran][0]} : {Id[ran][0]} --- {CName[ran][0]} ")
                    
                self.embed = Embed(
                title="Rolled Common",
                description=e,
                color=0xaa00b6 
                )
            case _ if 0.5 <= _roll < 0.8:
                self.embed = Embed(
                title="List of Cards",
                description=f"{_roll} uncommon",
                color=0xaa00b6 
                )
            case _ if 0.8 <= _roll < 0.95:
                self.embed = Embed(
                title="List of Cards",
                description=f"{_roll} rare",
                color=0xaa00b6 
                )
            case _ if 0.95 <= _roll < 0.98:
                self.embed = Embed(
                title="List of Cards",
                description=f"{_roll} ultra rare",
                color=0xaa00b6 
                )
            case _ if 0.99 <= _roll <= 1:
                self.embed = Embed(
                title="List of Cards",
                description=f"{_roll} legendary",
                color=0xaa00b6 
                )
        
    