import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="C@pu2003",
        database="workshop_archilog"
    )