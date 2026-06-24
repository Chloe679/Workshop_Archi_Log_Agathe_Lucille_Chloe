from config import get_connection

def getActivites():
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM activites ''')
    return mycursor.fetchall()

def createActivite(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur):
    mydb = get_connection()
    mycursor=mydb.cursor()
    sql ="INSERT INTO activites (titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur) VALUES(%s,%s, %s, %s, %s, %s, %s)"
    values =(titre_act, date_act, lieu_act, description_act, url_image_act, dangerosite_max_act, id_createur)

    mycursor.execute(sql, values)
    
    mydb.commit()

    mycursor.close()
    mydb.close()