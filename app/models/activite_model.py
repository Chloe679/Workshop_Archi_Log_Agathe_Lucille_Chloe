from config import get_connection

def getActivites():
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM activites ''')
    return mycursor.fetchall()

def getAnimal(id_user):
    mydb = get_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id_animal, nom_animal FROM animal WHERE id_user = %s", (id_user,))
    return mycursor.fetchall()


def createActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur):
    mydb = get_connection()
    mycursor=mydb.cursor()
    sql ="INSERT INTO activites (titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur) VALUES(%s,%s, %s, %s, %s, %s, %s)"
    values =(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur)

    mycursor.execute(sql, values)
    mydb.commit()
    id_act = mycursor.lastrowid 
    mycursor.close()
    mydb.close()
    return id_act 

def addAnimalActivite(id_act, id_user, id_animal):
    mydb = get_connection()
    mycursor=mydb.cursor()
    SQL ="INSERT INTO activites_animal_user (id_act, id_user, id_animal) VALUES(%s,%s, %s)"
    Values =(id_act, id_user, id_animal)
    mycursor.execute(SQL, Values)
    mydb.commit()
    mycursor.close()
    mydb.close()

def findID_act(activite_id):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM activites WHERE id_act = %s ''', (activite_id,))
    return mycursor.fetchone()