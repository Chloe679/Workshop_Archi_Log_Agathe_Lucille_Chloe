
from app.models.animal_model import Affiche, find_by_id,find_user_of_animal,find_commentaire, create_commentaire,create_fiche
from config import get_connection

def Affiche_Animal():
    resultat = Affiche()
    return resultat

def get_unique_animal(animal_id):
    return find_by_id(animal_id)

def get_proprio_animal(animal_id):
    return find_user_of_animal(animal_id)

def get_comm_animal(animal_id):
    return find_commentaire(animal_id)

def get_comm_animal(animal_id):
    resultats = find_commentaire(animal_id)
    return [comm[0] for comm in resultats]  # on extrait le texte de chaque tuple
   
def get_commentaire(commentaire,note,id_user,id_animal):
    return create_commentaire(commentaire,note,id_user,id_animal)

def addFiche(nom_animal,age_animal,type_animal,url_image_animal,description_animal,id_user,danger):
  return create_fiche(nom_animal,age_animal,type_animal,url_image_animal,description_animal,id_user,danger)


  