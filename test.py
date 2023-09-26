from DBhandler import get_rarity, get_cards

import random

Id, CName, Anime, Power, Type, Rarity, Image, cardCount = get_cards()
CCount, Common = get_rarity()

#row #colum #noidea

for i in range(20):
    ran = random.randint(0,CCount[0][0]-1)
    print(f"{Common[ran][0]} : {Id[ran][0]} --- {CName[ran][0]} ")

