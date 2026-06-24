from config import get_connection
from mysql.connector import Error

def RecupererLesInfosDuBoug(pseudo):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute("SELECT * FROM user WHERE username = %s",(pseudo,)) #Pour éviter d'extraire tout si on en a beaucoup
    return mycursor.fetchone()

def InscriptionDuBoug(pseudo, mdp, prenom, nom):
    mydb = get_connection()
    mycursor=mydb.cursor()
    sql ="INSERT INTO user (username, password, prenom_user, nom_user) VALUES(%s,%s, %s, %s)"
    values =(pseudo, mdp, prenom, nom)

    mycursor.execute(sql, values)
    
    mydb.commit()

    mycursor.close()
    mydb.close()