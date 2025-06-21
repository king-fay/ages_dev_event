import sqlite3

conn = sqlite3.connect('base.db')
def create():
    conn.execute('''
        CREATE TABLE Produit(
            id_prod INTEGER PRIMARY KEY AUTOINCREMENT ,
            nom TEXT not null,
            categorie INTEGER CHECK (categorie in (1,2,3)) not null,
            description TEXT not null,
            image TEXT not null
            );  
        
    ''')

    conn.commit()
    conn.close()

    print("base de donne et la table Produit est créer !!")

