from app.models.animal_model import Affiche, find_by_id

def Affiche_Animal():
    resultat = Affiche()
    return resultat

def get_unique_animal(animal_id):
    return find_by_id(animal_id)
