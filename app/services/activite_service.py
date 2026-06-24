from app.models.activite_model import getActivites
from app.models.activite_model import createActivite

def transferActivites():
    resultat = getActivites()
    return resultat

def addActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur):
    resultat = createActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur)
    return resultat