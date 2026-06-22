from flask import Flask, jsonify, render_template
from app.services.accueil_service import Affiche_Animal

main= Flask(__name__, template_folder='app/templates')


@main.route('/')
def AffichePage():
    return render_template("accueil.html")

@main.route('/Recupanimaux')
def recup_animaux():
    return jsonify(Affiche_Animal())

if __name__ == '__main__':
    main.run(debug=True)
