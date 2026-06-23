from app.models.animal_model import Affiche, find_by_id,find_user_of_animal,find_commentaire

def Affiche_Animal():
    resultat = Affiche()
    return resultat

def get_unique_animal(animal_id):
    return find_by_id(animal_id)

def get_proprio_animal(animal_id):
    return find_user_of_animal(animal_id)

def get_comm_animal(animal_id):
    return find_commentaire(animal_id)
   