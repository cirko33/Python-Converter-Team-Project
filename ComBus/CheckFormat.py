import sys
sys.path.insert(0, "..")
from HelperFunction.TakingSubstrings import take_substring_from_request
from curses.ascii import isalnum


def check_xml_format(xml_request):
    #Required fields
    if "verb" not in xml_request or "noun" not in xml_request:
        raise ValueError("BAD_FORMAT 5000")

    #Taking value of verb
    xml_verb = take_substring_from_request(xml_request, "<verb>", "</verb>")

    #Cheking value of verb
    if xml_verb not in ["GET", "POST", "DELETE", "PATCH"]:
        raise ValueError("BAD_FORMAT 5000")

    #Optional field
    if "query" in xml_request:
        #Taking value of query
        xml_query = take_substring_from_request(xml_request, "<query>", "</query>")

        #If there is any wrong character
        for char in xml_query:
            if not isalnum(char) and char not in [";", "=", "'", " "]:
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
        xml_field = take_substring_from_request(xml_request, "<fields>", "</fields>")

        #If there is any wrong character
        for char in xml_field:
            if char is not isalnum() and char not in [";", " "]:
                raise ValueError("BAD_FORMAT 5000")

    return "SUCCESS 2000"

    