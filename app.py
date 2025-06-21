from flask import Flask, render_template, jsonify, redirect, request, url_for
import sqlite3
from chargement import *
from flask_mail import Mail, Message
import os


ad={
    'nom':['agouda','bebou'],
    'prenom':['therese','faychal'],
    'code':['', '130539']
}

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='ucosangel@gmail.com',
    MAIL_PASSWORD='tjxq qmkm mbzp ytuu',
    MAIL_DEFAULT_SENDER='ucosangel@gmail.com'
)

mail = Mail(app)


@app.route('/')
def index():
    return render_template('tst.html')

@app.route('/produits')
def produit():
    n = request.args.get('categorie')
    prod = chargement(n)
    return jsonify(prod)

@app.route('/categorie')
def cat_p():
    n = request.args.get('cat')
    return render_template('def.html', prod=n)

@app.route('/admin', methods=["GET"])
def add():
    return render_template("admin.html", resultat='')

@app.route('/verification', methods=['POST'])
def verification():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    code = request.form.get('code')

    if nom in ad['nom']:
        i = ad['nom'].index(nom)
        if prenom == ad['prenom'][i]:
            if code ==ad['code'][i]:
                return render_template('pro.html', plc=tout())
            else:
                return render_template('admin.html', message = "erreur du code")
        else :
            return render_template('admin.html', message = "erreur du prenom")
    else:
        return redirect('/')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    cat = request.form.get('categorie')
    des = request.form.get('description')
    f = request.files['fichier']
    f.save('static/images/'+f.filename )
    ajout(cat, nom, des, f.filename)
    return render_template('pro.html', plc=tout())

@app.route('/sup')
def sup():
    id = request.args.get('id')
    supprimer(id)
    return render_template('pro.html', plc=tout())



@app.route('/envoyer', methods=['POST'])
def envoyer():
    """noms : noms,
          nom: nom,
          email: email,
          indicatif: indicatif,
          numero: numero,
          images: images,"""
    data = request.get_json()
    noms = data.get('noms')
    nom = data.get('nom')
    email = data.get('email')
    num = str(data.get('indicatif'))+str(data.get('numero'))
    nom_image = data.get('images')


    if email.strip():
        # 📁 Chemin absolu vers l'image locale
        image_path = os.path.join("D:/flask/Projet_Organisation/static/images", nom_image)

        # 📧 Préparation de l'email HTML avec image inline
        message = Message(subject="Image locale en pièce jointe", recipients=[email.strip()])
        message.html = f"""
        <h2>Bonjour {nom}</h2>
        <h2>ici agess dev nous vous contactons pour votre reservation de {noms} dont l'image si dessous</h2>
        <h2>nous tennons à savoir si cela tien toujours et si nous pouvons nous contacter sur {num}</h2>
        <h2>pour plus d'information cliquer <a href="https://wa.me/22870783376">ici</a> </h2>
        <img src="cid:image1">
        """

        with open(image_path, 'rb') as img:
            message.attach(nom_image, "image/jpeg", img.read(), disposition='inline', headers={'Content-ID': '<image1>'})

        mail.send(message)
        return jsonify({"data":"email envoyer avec succes"})
    else : return jsonify({"data":"erreur d'entré"})

if __name__=='__main__':
    app.run(debug=True)