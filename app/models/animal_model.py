from config import get_connection

def Affiche():
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM animal ''')
    return mycursor.fetchall()


def find_by_id(animal_id):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM animal WHERE id_animal = %s ''', (animal_id,)
    )
    return mycursor.fetchone() #on retourne une seule chose

#afficher nom du proprio
def find_user_of_animal(animal_id):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT prenom_user FROM user JOIN animal ON animal.id_user=user.id_user WHERE id_animal = %s ''', (animal_id,)
    )
    return mycursor.fetchone()