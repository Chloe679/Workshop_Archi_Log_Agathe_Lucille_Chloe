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

def ModifierLesInfosDuBougDansLaBDD(id_user, pseudoAncien, mdpAncien, prenomAncien, nomAncien, pseudoNouveau, mdpNouveau, prenomNouveau, nomNouveau):
    mydb = get_connection()
    mycursor=mydb.cursor()

    if not pseudoAncien == pseudoNouveau:
        sql = "UPDATE user SET username = %s WHERE id_user = %s;"
        values =(pseudoNouveau, id_user)
        mycursor.execute(sql, values)    

    if not prenomAncien == prenomNouveau:
        sql = "UPDATE user SET prenom_user = %s WHERE id_user = %s;"
        values =(prenomNouveau, id_user)
        mycursor.execute(sql, values)

    if not nomAncien == nomNouveau:
        sql = "UPDATE user SET nom_user = %s WHERE id_user = %s;"
        values =(nomNouveau, id_user)
        mycursor.execute(sql, values) 

    if not mdpAncien == mdpNouveau:
        sql = "UPDATE user SET password = %s WHERE id_user = %s;"
        values =(mdpNouveau, id_user)
        mycursor.execute(sql, values)
    
    mydb.commit()

    mycursor.close()
    mydb.close()