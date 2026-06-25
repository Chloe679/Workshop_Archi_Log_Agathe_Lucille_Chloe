from config import get_connection
import random

def get_random_id():
    mydb = get_connection()
    mycursor= mydb.cursor()
    mycursor.execute('''SELECT COUNT(id_animal) FROM animal ''')
    total = mycursor.fetchone()[0]  # récupère juste le nombre
    random_id = random.randint(1, total)  # génère un id aléatoire entre 1 et total
    mycursor.execute('''SELECT * FROM animal WHERE id_animal = %s''', (random_id,))
    return mycursor.fetchone()