from flask import Flask, jsonify, render_template
from app.services.animal_service import Affiche_Animal, get_unique_animal,get_proprio_animal,find_user_of_animal,get_comm_animal

main= Flask(__name__)


@main.route('/')
def AffichePageAccueil():
    return render_template("accueil.html")

@main.route('/activites')
def AffichePageActivites():
    return render_template("activite/accueil_activite.html")

@main.route('/connexion')
def AffichePageConnexion():
    return render_template("user/connexion.html")

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

@main.route('/Recupanimaux')
def recup_animaux():
    return jsonify(Affiche_Animal())

#Pour fiche animal 

@main.route('/animal/<int:animal_id>') #<int:animal_id> parmet de recup id de l'url
def AffichePageUniqueAnimaux(animal_id):
    return render_template("animal/fiche_animal.html", id=animal_id) #on donne l'id au template (pour utilser dans html)

@main.route('/Recup_unique_animal/<int:animal_id>') #on appelera dans le html /Recup_unique_animal/<int:animal_id>
def recup_unique_animal(animal_id):
    return jsonify(get_unique_animal(animal_id))

@main.route('/recup_propri_animal/<int:animal_id>')
def recup_propri_animal(animal_id):
    return jsonify(find_user_of_animal(animal_id))

@main.route('/recup_comm_animal/<int:animal_id>')
def recup_comm_animal(animal_id):
    return jsonify(get_comm_animal(animal_id))

if __name__ == '__main__':
    main.run(debug=True)
