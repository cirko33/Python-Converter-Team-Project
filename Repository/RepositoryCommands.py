from dataclasses import fields
from operator import index
import mysql.connector, sys
sys.path.insert(0, "..")
from mysql.connector import Error
from HelperFunction.TakingSubstrings import take_substring_from_request

def read_items(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception:
            cursor.close()
            connection.close()
            return ("REJECTED", 3000, "Not valid query for reading data")

        records = cursor.fetchall()

        def take_substring_from_request(request, begin_string, end_string):
            begin = request.find(begin_string) + len(begin_string)
            end = request.find(end_string)
            substring = request[begin : end]
            return substring

        query_noun = take_substring_from_request(query, "from ", " where")
        query_fields = take_substring_from_request(query, "select ", " from")
        query_values = tuple(records)

        ret_val = (query_noun, query_fields, query_values)
        cursor.close()
        connection.close()
        return ret_val
    else:
        return ("REJECTED", 3000, "Error at MySQL connection")

def execute_rest(query):
    connection = mysql.connector.connect(host="localhost", database="res", user="res_projekat", password="restim20")
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception:
            cursor.close()
            connection.close()
            return ("REJECTED", 3000, "Not valid query for modify data")
        
        connection.commit()

        splited_query = query.split(" ")
        query_verb = splited_query[0]

        if query_verb == "update":
            query_noun = splited_query[1]
        elif query_verb == "insert":
            noun = splited_query[2].split("(")
            query_noun = noun[0]
        else:
            query_noun = splited_query[2]

        ret_val = (query_noun, query_verb, cursor.rowcount)

        cursor.close()
        connection.close()
        return ret_val
    else:
        return ("REJECTED", 3000, "Error at MySQL connection")


def send_request(query):
    if query.startswith('select'):
        return read_items(query)
    else:
        return execute_rest(query)