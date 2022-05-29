from cmath import e
from multiprocessing import connection
from types import NoneType
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages

def read_items(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(query)
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
        cursor.execute(query)
        connection.commit()
        retVal = cursor.rowcount

        cursor.close()
        connection.close()
        return retVal
    else:
        raise Error(msg="Error in MySQL connection")