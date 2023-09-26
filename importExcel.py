import sqlite3
import pandas as pd

path = "Book.xlsx"
file = pd.ExcelFile(path)
df = pd.read_excel(file, sheet_name='Sheet1')

con = sqlite3.connect('VoidCards.db') 
c = con.cursor()


c.execute("""DROP TABLE IF EXISTS Cards""")
c.execute("""
    CREATE TABLE Cards (
        Id TEXT,
        Name TEXT,
        Anime TEXT,
        Power TEXT,
        Type TEXT,
        Rarity TEXT,
        Image TEXT
    )
""")


for row in df.itertuples(index=False):
    
    c.execute("""
        INSERT INTO Cards ("Id","Name", "Anime", "Power", "Type", "Rarity", "Image")
        VALUES (CAST(? AS TEXT),?, ?, CAST(? AS TEXT), ?, ?, ?)
    """, (row.Id, row.Name, row.Anime, row.Power, row.Type, row.Rarity, row.Image))

con.commit()
c.close()
print("uploaded")