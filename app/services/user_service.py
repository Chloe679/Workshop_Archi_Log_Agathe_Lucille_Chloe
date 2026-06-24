from app.models.user_model import RecupererLesInfosDuBoug, InscriptionDuBoug
from werkzeug.security import check_password_hash, generate_password_hash


def estCeQueLeBougExiste(pseudoDuBoug, mdpDuBoug):
    utilisateur = RecupererLesInfosDuBoug(pseudoDuBoug)

    if utilisateur is None:
        return None

    pseudo = utilisateur[1]
    mot_de_passe = utilisateur[2]

    if pseudo == pseudoDuBoug and check_password_hash(mot_de_passe, mdpDuBoug):
        return utilisateur

    return None

def ajouterLeBougDansLaBDD(pseudo, mdp, prenom, nom):
    mdp_hache = generate_password_hash(mdp)
    resultat = InscriptionDuBoug(pseudo, mdp_hache, prenom, nom)
    return resultat