from flask import Flask, jsonify, render_template
from app.services.accueil_service import Affiche_Animal

main= Flask(__name__, template_folder='app/templates')

@main.route('/')
def recup_animaux():
    return jsonify(Affiche_Animal())

@main.route('/Recupanimaux')
def AffichePage():
    return render_template("app/templates/accueil.html")

if __name__ == '__main__':
    main.run(debug=True)
