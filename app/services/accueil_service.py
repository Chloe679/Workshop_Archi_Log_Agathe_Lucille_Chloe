from app.models.accueil_model import Affiche

def Affiche_Animal():
    listeAnimal = []
    resultat = Affiche()
    for animal in resultat:
        listeAnimal.append(animal)
    return listeAnimal
