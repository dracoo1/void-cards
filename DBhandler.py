import sqlite3
global users
global cards
global card
global count
users = None
cards = None
card = None
count = None


def checkExist():
    con = sqlite3.connect("VoidCards.db")
    cur = con.cursor()
    
    try:
        cur.execute("CREATE TABLE Users(Id,UserID, Name, G, Shards, Cards)")
    except:
        print("users already exists")

    try:
        cur.execute("CREATE TABLE Cards(Name, Anime, Power, Type, Rarity, Image)")
    except:
        print("cards already exists")


def get_cards():
    con = sqlite3.connect("VoidCards.db")
    cur = con.cursor()

    res = cur.execute("SELECT COUNT(*) FROM Cards")
    cardCount = res.fetchall()[0][0]
    res = cur.execute("SELECT Id FROM Cards")
    Id=res.fetchall()
    res = cur.execute("SELECT Name FROM Cards")
    CName=res.fetchall()
    res = cur.execute("SELECT Anime FROM Cards")
    Anime=res.fetchall()
    res = cur.execute("SELECT Power FROM Cards")
    Power=res.fetchall()
    res = cur.execute("SELECT Type FROM Cards")
    Type=res.fetchall()
    res = cur.execute("SELECT Rarity FROM Cards")
    Rarity=res.fetchall()
    res = cur.execute("SELECT Image FROM Cards")
    Image=res.fetchall()
    return Id, CName, Anime, Power, Type, Rarity, Image, cardCount

def get_rarity():
    con = sqlite3.connect("VoidCards.db")
    cur = con.cursor()
    
    res = cur.execute("SELECT COUNT(*) FROM Cards WHERE Rarity=?", ("Common",))
    CCount = res.fetchall()
    res = cur.execute("SELECT Id FROM Cards WHERE Rarity=?", ("Common",))
    Common = res.fetchall()
    
    return CCount, Common


def get_user():
    con = sqlite3.connect("VoidCards.db")
    cur = con.cursor()
    
    res = cur.execute("SELECT COUNT(*) FROM Users")
    playerCount = res.fetchall
    res = cur.execute("SELECT Name FROM Users")
    UName=res.fetchall()
    res = cur.execute("SELECT UserID FROM Users")
    UserID=res.fetchall()
    res = cur.execute("SELECT G FROM Users")
    G=res.fetchall()
    res = cur.execute("SELECT Shards FROM Users")
    Shards=res.fetchall()    
    res = cur.execute("SELECT Cards FROM Users")
    Cards=res.fetchall()    
    return UserID, UName, G, Shards, Cards, playerCount

def usuer_update():
    con = sqlite3.connect("VoidCards.db")
    cur = con.cursor
    
    res = cur.execute("")
def update():
    print("test")

checkExist()
#get_data()
