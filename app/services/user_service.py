from app.models.user_model import RecupererLesInfosDuBoug, InscriptionDuBoug, ModifierLesInfosDuBougDansLaBDD
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

def ModifierLesInfosDuBoug(id_user, pseudoAncien, mdpAncien, prenomAncien, nomAncien, pseudoNouveau, mdpNouveau, prenomNouveau, nomNouveau):
    if mdpNouveau and not check_password_hash(mdpAncien, mdpNouveau):
        mdp_hache_Nouveau = generate_password_hash(mdpNouveau)
    else:
        mdp_hache_Nouveau = mdpAncien
    resultat = ModifierLesInfosDuBougDansLaBDD(id_user, pseudoAncien, mdpAncien, prenomAncien, nomAncien, pseudoNouveau, mdp_hache_Nouveau, prenomNouveau, nomNouveau)
    return resultat