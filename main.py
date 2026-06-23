from flask import Flask, jsonify, render_template
from app.services.accueil_service import Affiche_Animal

main= Flask(__name__)


@main.route('/')
def AffichePageAccueil():
    return render_template("accueil.html")

@main.route('/activites')
def AffichePageActivites():
    return render_template("activite/accueil_activite.html")

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

@main.route('/connexion')
def AffichePageConnexion():
    return render_template("user/connexion.html")

@main.route('/Recupanimaux')
def recup_animaux():
    return jsonify(Affiche_Animal())

if __name__ == '__main__':
    main.run(debug=True)
