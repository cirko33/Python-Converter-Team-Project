import mysql.connector
from mysql.connector import Error

def read_items(query, usr, passw):
    try:
        connection = mysql.connector.connect(host="localhost", database="res", user=str(usr), password=str(passw))
        cursor = connection.cursor()
        cursor.execute(query)
    except Exception:
        if connection.is_connected():
            message = "Not valid query for reading data"
        else:
            message = "Error at MySQL connection"
        cursor.close()
        connection.close()
        return ("REJECTED", 3000, message)
    records = cursor.fetchall()
    def take_substring_from_request(request, begin_string, end_string):
        begin = request.find(begin_string) + len(begin_string)
        end = request.find(end_string)
        substring = request[begin : end]
        return substring
    query_noun = take_substring_from_request(query, "from ", " where")
    query_fields = take_substring_from_request(query, "select ", " from")
    query_values = list(records)
    ret_val = (query_noun, query_fields, query_values)
    cursor.close()
    connection.close()
    return ret_val

def execute_rest(query, usr, passw):
    try:
        connection = mysql.connector.connect(host="localhost", database="res", user=str(usr), password=str(passw))
        cursor = connection.cursor()
        cursor.execute(query)
    except Exception:
        if connection.is_connected():
            message = "Not valid query for reading data"
        else:
            message = "Error at MySQL connection"
        cursor.close()
        connection.close()
        return ("REJECTED", 3000, message)
    
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


def send_request(query):
    file = open("RepositoryAuthentification.txt")
    username = file.readline()
    password = file.readline()
    file.close();
    if query.startswith('select'):
        return read_items(query, username, password)
    else:
        return execute_rest(query, username, password)