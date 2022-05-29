from cmath import e
from multiprocessing import connection
from types import NoneType
import unittest
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages

def read_items(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error:
            cursor.close()
            connection.close()
            raise Exception("Not valid query for reading data")

        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records
    else:
        raise Exception("Error in MySQL connection")

def execute_rest(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error:
            cursor.close()
            connection.close()
            raise Exception("Not valid query for modify data")
        
        connection.commit()
        retVal = cursor.rowcount

        cursor.close()
        connection.close()
        return retVal
    else:
        raise Exception(msg="Error in MySQL connection")

