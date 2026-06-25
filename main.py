from flask import Flask, jsonify, render_template,request, redirect, url_for, flash, session
from app.services.animal_service import Affiche_Animal, get_unique_animal,get_proprio_animal,find_user_of_animal,get_comm_animal,get_commentaire,addFiche,affiche_moyenne
from app.services.activite_service import transferActivites, addActivite, getFicheActivite, transferAnimal, linkAnimal, removeActivite
from app.services.user_service import estCeQueLeBougExiste, ajouterLeBougDansLaBDD, ModifierLesInfosDuBoug, RecupererLesAnimauxDuBoug, RecupererLesActivitesDuBoug
from werkzeug.security import check_password_hash
from app.services.accueil_service import affiche_random_id

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

@main.route('/inscription', methods=['GET', 'POST'])
def AffichageInscription():
    if request.method =='GET':
        return render_template("user/inscription.html")
    
    try:
        donnees = request.form
        pseudo = donnees.get('pseudo') #récup le pseudo saisi
        mdp = donnees.get('mdp') #récup le mdp saisie
        prenom = donnees.get('prenom') #récup le mdp saisie
        nom = donnees.get('nom') #récup le mdp saisie

        ajouterLeBougDansLaBDD(pseudo, mdp, prenom, nom)

        utilisateur = estCeQueLeBougExiste(pseudo, mdp) 
        session['id_utilisateur'] = utilisateur[0]
        session['pseudo_utilisateur'] = utilisateur[1]
        session['mdp_utilisateur'] = utilisateur[2]
        session['prenom_utilisateur'] = utilisateur[3]
        session['nom_utilisateur'] = utilisateur[4]

        flash("Utilisateur créé.", "success")
        return redirect(url_for('affichageCompteUtilisateur'))
    
    except ValueError as error:
        flash(str(error), "error")
        return render_template("user/inscription.html")
    
@main.route('/ModificationUser', methods=['GET', 'POST'])
def affichageModifCompteUtilisateur():
    if request.method =='GET':
        return render_template("user/accountModification.html")
    
    try:
        donnees = request.form
        pseudo = donnees.get('pseudo') #récup le pseudo saisi
        mdpActuel = donnees.get('mdpActuel') #récup le mdp saisie
        mdpModif = donnees.get('mdpModif') #récup le mdp saisie
        prenom = donnees.get('prenom') #récup le mdp saisie
        nom = donnees.get('nom') #récup le mdp saisie

        if not mdpModif:
            mdpModif = mdpActuel

        try:
            mdp_actuel_valide = check_password_hash(session['mdp_utilisateur'], mdpActuel)
        except (ValueError, TypeError):
            mdp_actuel_valide = False #Evite les erreurs si corrompu, vide ou mauvais format
        
        if mdp_actuel_valide:

            ModifierLesInfosDuBoug(session['id_utilisateur'], session['pseudo_utilisateur'], session['mdp_utilisateur'], session['prenom_utilisateur'], session['nom_utilisateur'], pseudo, mdpModif, prenom, nom)

            flash("Compte mis à jour. Veuillez vous reconnecter.", "success")
            return redirect(url_for('deconnexion'))
        else:
            flash("Mot de passe actuel incorrect.", "error")
            return render_template("user/accountModification.html")
    
    except ValueError as error:
        flash(str(error), "error")
        return render_template("user/accountModification.html")
    
@main.route('/RecupAnimauxDuBoug')
def recup_animauxDuBoug():
    return jsonify(RecupererLesAnimauxDuBoug(session['id_utilisateur']))

@main.route('/RecupActivitesDuBoug')
def recup_activitesDuBoug():
    return jsonify(RecupererLesActivitesDuBoug(session['id_utilisateur']))

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

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

@main.route('/activites/<int:activite_id>') 
def afficheFicheActivite(activite_id):
    return render_template("activite/fiche_activite.html", id=activite_id) #on donne l'id au template (pour utilser dans html)

@main.route('/Recup_fiche_activite/<int:activite_id>') 
def recup_fiche_activite(activite_id):
    return jsonify(getFicheActivite(activite_id))

@main.route('/delete_activite/<int:activite_id>', methods=['POST'])
def suppActivite(activite_id):
    print("Suppression activite id:", activite_id)
    removeActivite(activite_id)
    flash("Activité supprimée.", "success")
    return redirect(url_for('AffichePageActivites'))
    

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

@main.route('/create_animal', methods=['GET','POST'])

def AfficheCreateFiche():
    if request.method =='GET':
        return render_template("animal/create_animal.html")
    
    try:

        id_user_connected = session['id_utilisateur']; #A remplacer avec l'id de l'utilisateur connecté quand on aura merge

        id_act = addFiche(
            nom_animal = request.form.get("nom_animal"),
            age_animal = request.form.get("age_animal"),
            type_animal = request.form.get("type_animal"),
            url_image_animal = request.form.get("url_image_animal"),
            description_animal = request.form.get("description_animal"),
            id_user = id_user_connected,
            danger = request.form.get("danger")
        )
        flash("Fiche créée.", "success")
        return redirect(url_for('AffichePageAnimal'))
    
    except ValueError as error:
        flash(str(error), "error")
        return render_template("animal/create_animal.html")

#route pour aller page créer fiche animal
@main.route('/animal')
def AffichePageAnimal():
    return render_template("animal/accueil_animal.html")

@main.route('/moyenne_animal/<int:animal_id>')
def moyenne_animal(animal_id):
    return jsonify(affiche_moyenne(animal_id))

@main.route('/affichage_random')
def affiche_random():
    return jsonify(affiche_random_id())


if __name__ == '__main__':
    main.run(debug=True)

