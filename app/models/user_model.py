from config import get_connection
from mysql.connector import Error

def RecupererLesInfosDuBoug(pseudo):
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute("SELECT username, password FROM user WHERE username = %s",(pseudo,)) #Pour éviter d'extraire tout si on en a beaucoup
    return mycursor.fetchall()