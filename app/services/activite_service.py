from app.models.activite_model import getActivites
from app.models.activite_model import createActivite, findID_act, getAnimal, addAnimalActivite

def transferActivites():
    resultat = getActivites()
    return resultat

def addActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur):
    resultat = createActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur)
    return resultat

def transferAnimal(id_user):
    resultat = getAnimal(id_user)
    return resultat

def linkAnimal(id_act, id_user, id_animal):
    resultat = addAnimalActivite(id_act, id_user, id_animal)
    return resultat


def getFicheActivite(activite_id):
    return findID_act(activite_id)