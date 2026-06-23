from app.models.user_model import RecupererLesInfosDuBoug

def estCeQueLeBougExiste(pseudoDuBoug, mdpDuBoug):
    utilisateurs = RecupererLesInfosDuBoug(pseudoDuBoug)

    for utilisateur in utilisateurs:
        pseudo = utilisateur[0]
        mot_de_passe = utilisateur[1]

        if pseudo == pseudoDuBoug and mot_de_passe == mdpDuBoug:
            return utilisateur

    return None 