from flask import Flask, jsonify, render_template,request, redirect, url_for, flash, session
from app.services.animal_service import Affiche_Animal, get_unique_animal,get_proprio_animal,find_user_of_animal,get_comm_animal,get_commentaire
from app.services.activite_service import transferActivites, addActivite, getFicheActivite, transferAnimal, linkAnimal
from app.services.user_service import estCeQueLeBougExiste

main= Flask(__name__)
main.secret_key = "455771a41b3d2853dc7876378211876f860cf61512d49f8d0418bb94649056c9"
# Si mis en ligne, à masquer

@main.route('/')
def AffichePageAccueil():
    return render_template("accueil.html")

######################################################## ROUTES UTILISATEURS ########################################################

@main.route('/connexion', methods=["POST", "GET"])
def AffichePageConnexion():
    if request.method == "POST":
        donnees = request.form
        pseudo = donnees.get('pseudo') #récup le pseudo saisi
        mdp = donnees.get('mdp') #récup le mdp saisie

        utilisateur = estCeQueLeBougExiste(pseudo, mdp) #Vérifie si l'utilisateur est dans la BDD

        if utilisateur is not None: #
            session['id_utilisateur'] = utilisateur[0]
            session['pseudo_utilisateur'] = utilisateur[1]
            session['mdp_utilisateur'] = utilisateur[2]
            session['prenom_utilisateur'] = utilisateur[3]
            session['nom_utilisateur'] = utilisateur[4]
            print(session)
            return redirect(url_for('AffichePageAccueil'))
        else :
            print("utilisateur inconnu")
            return redirect(request.url)
    else :
        if 'pseudo_utilisateur' in session:
            return redirect(url_for('AffichePageAccueil'))
        return render_template("user/connexion.html")
    
@main.route('/deconnexion')
def deconnexion():
    session.clear()
    return redirect(url_for('AffichePageConnexion'))

@main.route('/compteUtilisateur')
def affichageCompteUtilisateur():
    return render_template("user/account.html")

######################################################## ROUTES ACTIVTES ########################################################

@main.route('/activites')
def AffichePageActivites():
    return render_template("activite/accueil_activite.html")

@main.route('/create_activite', methods=['GET', 'POST'])
def AfficheCreateActivite():
    if request.method =='GET':
        animaux = transferAnimal(session['id_utilisateur'])
        return render_template("activite/create_activite.html", animaux=animaux)
    
    try:

        id_user_connected = session['id_utilisateur']; 
        id_act = addActivite(
            titre_act = request.form.get("titre_act"),
            date_act = request.form.get("date_act"),
            lieu_act = request.form.get("lieu_act"),
            description_act = request.form.get("description_act"),
            url_image_act = request.form.get("url_image_act"),
            dangerosite_max_act = request.form.get("dangerosite_max_act"),
            id_createur = session['id_utilisateur']
        )
        animaux_selected = request.form.getlist("animaux")
        for id_animal in animaux_selected :
            linkAnimal(id_act, session['id_utilisateur'], id_animal)

        flash("Activité créée.", "success")
        return redirect(url_for('AffichePageActivites'))
    
    except ValueError as error:
        flash(str(error), "error")
        animaux = transferAnimal(session['id_utilisateur'])
        return render_template("activite/create_activite.html", animaux=animaux)

######################################################## AUTRES ########################################################

######################################################## AUTRES ########################################################

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

@main.route('/activites/<int:activite_id>') 
def afficheFicheActivite(activite_id):
    return render_template("activite/fiche_activite.html", id=activite_id) #on donne l'id au template (pour utilser dans html)

@main.route('/Recup_fiche_activite/<int:activite_id>') 
def recup_fiche_activite(activite_id):
    return jsonify(getFicheActivite(activite_id))



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

@main.route('/animal/<int:animal_id>/commentaire', methods=(['GET','POST']))
def affiche_create_comm(animal_id):
    if request.method=='GET':
        return render_template("animal/fiche_animal.html", id=animal_id)
    try:
        id_user_connecte= session['id_utilisateur']
        get_commentaire(
            commentaire= request.form.get("commentaire"),
            note=request.form.get("note"),
            id_user=id_user_connecte,
            id_animal= animal_id
        )
        flash("Commentaire ajouté.", "success")
        return redirect(url_for('AffichePageUniqueAnimaux', animal_id=animal_id))

    except ValueError as error:
        flash(str(error), "error")
        return render_template("animal/fiche_animal.html", id=animal_id)
        
@main.route('/infosActivites')
def recup_activites():
    return jsonify(transferActivites())

if __name__ == '__main__':
    main.run(debug=True)
