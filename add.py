import sqlite3
con = sqlite3.connect("VoidCards.db")
cur = con.cursor()

Name = None
Anime= None
Power = None
Defence = None
Type = None
Effect = None
Rarity = None
Imagename = None

Name = input("Card Name: ")
Anime = input("Anime Name: ")
Power = input("Card Power: ")
Type = input("Card Type: ")
Rarity = input("Card Rarity: ")
Imagename = input("Card Image Name: ")

print (Name, Power, Type, Rarity, Imagename)


try:
    cur.execute("INSERT INTO Cards (Name, Anime, Power, Type, Rarity, Image) VALUES (?, ?, ?, ?, ?, ?)", (Name, Anime, Power, Type, Rarity, Imagename))
    
    # Commit the changes to the database
    con.commit()
    
    print("Data inserted successfully.")
except sqlite3.Error as e:
    print("Error:", e)
    con.rollback()  # Rollback the transaction in case of an error

# Close the database connection
con.close()