import mysql.connector
from mysql.connector.errors import *

from skilly.package import package


import importlib.util

file_path = "./config.py"
module_name = file_path.replace("/", ".")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


mydb = mysql.connector.connect(
    host=module.database['host'],
    user=module.database['user'],
    database=module.database['db-name'],
    password=module.database['password']
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

