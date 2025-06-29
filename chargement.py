import sqlite3
from flask import jsonify, request
import requests

def chemin(image_filename):
    base_url = request.host_url  # récupère https://ton-app.onrender.com/
    return "http://127.0.0.1:5000"+'/static/images/' + image_filename


class objet():
    categorie : int
    descript : str
    image : str
    def __init__(self, cat, des, im):
        self.categorie = cat
        self.descript = des
        self.image = im

def chargement(cat):
    conn = sqlite3.connect('base.db')
    #conn.row_factory = sqlite3.Row
    table = conn.execute("SELECT description,nom, image from Produit where categorie = ?", (cat,)).fetchall()
    conn.close()
    return table

def ajout(cat,nom, des, img):
    conn = sqlite3.connect("base.db")
    conn.row_factory = sqlite3.Row
    conn.execute("Insert into Produit (categorie,nom, description , image) values (?,?,?,?)",(cat,nom, des, img))
    conn.commit()
    conn.close()
    print("ajouté avec succès")

def tout():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_prod, nom, categorie, description, image FROM Produit")
    table = cursor.fetchall()  # This returns a list of tuples (each row as a tuple)
    conn.close()
    return table


def modifier_donnees(id, nouveau_nom):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE ma_table SET image = ? WHERE id = ?", (nouveau_nom, id))
    conn.commit()
    conn.close()

def supprimer(id):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produit WHERE id_prod = ?", (id,))
    conn.commit()
    conn.close()
    print("supprimer avec succès")


def envoyerm(numero, image_url, texte):
    numero = numero.replace(" ","")
    url = 'https://graph.facebook.com/v19.0/646976848507542/messages'
    token = "EAAT4mcBcJ54BO5TPRZA7bOuAmvfRCCxlUV2dcAzKBInBpzY6B9VIKzpP9EYF3qJHekNkhD8vrdqMVscd2qJuZAp0nDLOeD9zkR5JLZBTMm7NjkYdJDlmmHMZAxsTrJtVZA6Qx8gDrtPTnIpXorJqRxWMUXHgllLajM87ZCBITJPZBRMB3NO1XNraaeRccbogQaIexhKpxjrOjIOmZA8Uv1koXdZB91RBr8WwgkK59A4hTlXNZCFGRm"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    image_url= chemin(str(image_url))
    
    """payload = {
        'messaging_product': 'whatsapp',
        'to': numero,
        'type': 'image',
        'image': {
            'link': image_url,
            'caption': texte
        }
    }"""
    payload = {
    "messaging_product": "whatsapp",
    "to": numero,
    "type": "text",
    "text": {
        "body": "Hello depuis Flask 🧪"
    }
    }


    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)
    print(response.json())
