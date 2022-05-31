from ast import If
from curses.ascii import isalnum, isalpha
from dataclasses import field
from posixpath import split
from xml.dom import ValidationErr


def check_xml_format(xml_request):
    #Required fields
    if "verb" not in xml_request or "noun" not in xml_request:
        raise ValueError("BAD_FORMAT 5000")

    #Taking value of verb
    begin = xml_request.find("<verb>") + len("<verb>")
    end = xml_request.find("</verb>")
    xml_verb = xml_request[begin : end]

    #Cheking value of verb
    if xml_verb not in ["GET", "POST", "DELETE", "PATCH"]:
        raise ValueError("BAD_FORMAT 5000")

    #Optional field
    if "query" in xml_request:
        #Taking value of query
        begin = xml_request.find("<query>") + len("<query>")
        end = xml_request.find("</query>")
        xml_query = xml_request[begin : end]

        #If there is any wrong character
        for char in xml_query:
            if char is not isalnum() and char not in [";", "=", "'", " "]:
                raise ValueError("BAD_FORMAT 5000")

        #Does every query have '=' 
        queries = xml_query.split(";")
        for query in queries:
            if "=" not in query:
                raise ValueError("BAD_FORMAT 5000")

    #Optional field
    if "fields" in xml_request:
        #Only apears when verb is GET
        if xml_verb is not "GET":
            raise ValueError("BAD_FORMAT 5000")
        
        #Taking fields
        begin = xml_request.find("<fields>") + len("<fields>")
        end = xml_request.find("</fields>")
        xml_field = xml_request[begin : end]

        #If there is any wrong character
        for char in xml_field:
            if char is not isalnum() and char not in [";", " "]:
                raise ValueError("BAD_FORMAT 5000")

    return "SUCCESS 2000"

    