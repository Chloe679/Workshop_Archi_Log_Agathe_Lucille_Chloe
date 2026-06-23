from app.models.user_model import RecupererLesInfosDuBoug

def estCeQueLeBougExiste(pseudoDuBoug, mdpDuBoug):
    utilisateur = RecupererLesInfosDuBoug(pseudoDuBoug)

    if utilisateur is None:
        return None

    pseudo = utilisateur[1]
    mot_de_passe = utilisateur[2]

    if pseudo == pseudoDuBoug and mot_de_passe == mdpDuBoug:
        return utilisateur

    return None
