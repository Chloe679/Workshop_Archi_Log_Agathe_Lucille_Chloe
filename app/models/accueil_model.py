from config import get_connection

def Affiche():
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT * FROM animal ''')
    return mycursor.fetchall()