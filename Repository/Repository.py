from multiprocessing import connection
from types import NoneType
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages

class Repository:
    def __init__(self):
        connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")

    def execute_sql(self, query):
        query1 = query.lower()
        if "select" in query1:
            self.__read_items(query)
        else:
            self.__execute_rest(query)   

    def __read_items(self, query):
        try:
            connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()

            print("Number of rows: ", cursor.rowcount)

            print("\nPrinting rows: ")

            for row in records:
                print("Id: ", row[0], " ")
                print("Name: ", row[1], " ")
                print("Last name: ", row[2], " ")
                print("Username: ", row[3], " ")
                print("Email: ", row[4], " ")

                if "profesor" in query:
                    print("Department = ", row[5], "\n")
                elif "student" in query:
                    print("Year of study = ", row[5], "\n")

        except Error as e:
            print("Error in MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("\nMySQL connection is closed!!!\n")

    def __execute_rest(self, query):
        try:
            connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

            print(cursor.rowcount, "row", end=" ")
            if cursor.rowcount > 1:
                print("s are ", end = " ")
            else:
                print(" is ", end = " ")
            query1 = query.lower()
            x = query1.split(" ")

            if  "insert" in query1:
                print(x[0] + "ed\n")
            else:
                print(x[0] + "d\n");

        except Error as e:
            print("Error in MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("\nMySQL connection is closed!!!\n")