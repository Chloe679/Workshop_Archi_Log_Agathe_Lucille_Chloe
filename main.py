from flask import Flask, jsonify, render_template, redirect, request, flash, url_for
from app.services.accueil_service import Affiche_Animal
from app.services.activite_service import transferActivites, addActivite

main= Flask(__name__)
main.secret_key = "455771a41b3d2853dc7876378211876f860cf61512d49f8d0418bb94649056c9"

@main.route('/')
def AffichePageAccueil():
    return render_template("accueil.html")

@main.route('/activites')
def AffichePageActivites():
    return render_template("activite/accueil_activite.html")

@main.route('/create_activite', methods=['GET', 'POST'])
def AfficheCreateActivite():
    if request.method =='GET':
        return render_template("activite/create_activite.html")
    
    try:

        id_user_connected = 1 #A remplacer avec l'id de l'utilisateur connecté quand on aura merge

        id_act = addActivite(
            titre_act = request.form.get("titre_act"),
            date_act = request.form.get("date_act"),
            lieu_act = request.form.get("lieu_act"),
            description_act = request.form.get("description_act"),
            url_image_act = request.form.get("url_image_act"),
            dangerosite_max_act = request.form.get("dangerosite_max_act"),
            id_createur = id_user_connected
        )
        flash("Activité créée.", "success")
        return redirect(url_for('AffichePageActivites'))
    
    except ValueError as error:
        flash(str(error), "error")
        return render_template("activite/create_activite.html")

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

@main.route('/connexion')
def AffichePageConnexion():
    return render_template("user/connexion.html")

@main.route('/Recupanimaux')
def recup_animaux():
    return jsonify(Affiche_Animal())

@main.route('/infosActivites')
def recup_activites():
    return jsonify(transferActivites())

if __name__ == '__main__':
    main.run(debug=True)
