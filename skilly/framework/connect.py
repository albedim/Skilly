import mysql.connector
from mysql.connector.errors import *


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="prova",
    password=""
)

cursor = mydb.cursor(buffered=True)


def commit(query):
    try:
        cursor.execute(query)
        mydb.commit()
        mydb.reset_session()
    except InterfaceError:
        print("Unable to connect to {}")
        return None
    except():
        mydb.rollback()


def get(query, fetchAll):
    try:
        cursor.execute(query)
        r = cursor.fetchall() if fetchAll else cursor.fetchone()
        return r
    except InterfaceError:
        print("Unable to connect to {}")
        return [] if fetchAll else None
    except():
        mydb.rollback()


def delete(query, fetchAll):
    try:
        r = get(query.replace("DELETE", f"SELECT *"), fetchAll)
        cursor.execute(query)
        mydb.commit()
        return r
    except InterfaceError:
        print("Unable to connect to {}")
        return [] if fetchAll else None
    except():
        mydb.rollback()

