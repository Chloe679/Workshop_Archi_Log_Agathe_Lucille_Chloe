from flask import Flask, jsonify, render_template, session, request, redirect, url_for
from app.services.accueil_service import Affiche_Animal
from app.services.user_service import estCeQueLeBougExiste

main= Flask(__name__)
main.secret_key = "455771a41b3d2853dc7876378211876f860cf61512d49f8d0418bb94649056c9"
# Si mis en ligne, à masquer

@main.route('/')
def AffichePageAccueil():
    return render_template("accueil.html")

@main.route('/activites')
def AffichePageActivites():
    return render_template("activite/accueil_activite.html")

@main.route('/animaux')
def AffichePageAnimaux():
    return render_template("animal/accueil_animal.html")

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

######################################################## AUTRES ########################################################

@main.route('/Recupanimaux')
def recup_animaux():
    return jsonify(Affiche_Animal())

if __name__ == '__main__':
    main.run(debug=True)
