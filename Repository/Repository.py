import mysql.connector
from mysql.connector import Error

def read_items(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception:
            cursor.close()
            connection.close()
            raise Error("Not valid query for reading data")

        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records
    else:
        raise Error("Error in MySQL connection")

def execute_rest(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception:
            cursor.close()
            connection.close()
            raise Error("Not valid query for modify data")
        
        connection.commit()
        ret_val = cursor.rowcount

        cursor.close()
        connection.close()
        return ret_val
    else:
        raise Error("Error in MySQL connection")