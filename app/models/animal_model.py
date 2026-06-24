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
    return mycursor.fetchall()

#afficher les commentaires et la note associés à l'animal
def find_commentaire(animal_id):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT commentaire, note FROM commentaire JOIN animal ON animal.id_animal=commentaire.id_animal WHERE animal.id_animal  = %s ''', (animal_id,)
    )
    return mycursor.fetchall()

#creation des commentaires

def create_commentaire(commentaire,note,id_user,id_animal): 
    mydb = get_connection()
    mycursor= mydb.cursor()
    sql='''INSERT INTO commentaire (commentaire,note,id_user,id_animal) VALUES (%s,%s,%s,%s)''' 
    values=(commentaire,note,id_user,id_animal)
    mycursor.execute(sql, values)
    mydb.commit()
    mycursor.close()
    mydb.close()
