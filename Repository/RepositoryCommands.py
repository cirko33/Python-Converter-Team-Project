import mysql.connector
from mysql.connector import Error

# def load():
#     file = open("RepositoryAuthentication.txt")
#     username = file.readline()
#     password = file.readline()
#     file.close();
#     return username, password

mysql_host = "localhost"
mysql_database = "res"
mysql_user, mysql_password = "res_projekat", "restim20"

config = {
    'host' : mysql_host,
    'database' : mysql_database,
    'user' : str(mysql_user),
    'password' : str(mysql_password)
}

def read_items(query):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
    except Error as err:
        return ("REJECTED", 3000, f"Error at MySQL connection: {err}")

    try:
        cursor.execute(query)
    except Exception as e:
        cursor.close()
        connection.close()

        return ("REJECTED", 3000, f'Not valid query for reading data: {e}')

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

def execute_rest(query):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
    except Error as err:
        return ("REJECTED", 3000, f"Error at MySQL connection: {err}")

    try:
        cursor.execute(query)
    except Exception as e:
        cursor.close()
        connection.close()

        return ("REJECTED", 3000, f'Not valid query for modify data: {e}')
    
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
    if query.startswith('select'):
        return read_items(query)
    else:
        return execute_rest(query)

