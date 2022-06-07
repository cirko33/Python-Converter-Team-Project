

def check_xml_format(xml_request):
    #Required fields
    if "verb" not in xml_request or "noun" not in xml_request:
        return "BAD_FORMAT 5000"

    def take_substring_from_request(request, begin_string, end_string):
        begin = request.find(begin_string) + len(begin_string)
        end = request.find(end_string)

        substring = request[begin : end]

        return substring

    #Taking value of verb
    xml_verb = take_substring_from_request(xml_request, "<verb>", "</verb>")

    #Cheking value of verb
    if xml_verb not in ["GET", "POST", "DELETE", "PATCH"]:
        return "BAD_FORMAT 5000"

    #Optional field
    if "query" in xml_request:
        #Taking value of query
        xml_query = take_substring_from_request(xml_request, "<query>", "</query>")

        #If there is any wrong character
        for char in xml_query:
            if not char.isalnum() and char not in [";", "=", "'", " "]:
                return "BAD_FORMAT 5000"

        #Does every query have '=' 
        queries = xml_query.split(";")
        for query in queries:
            if "=" not in query:
                return "BAD_FORMAT 5000"

    #Optional field
    if "fields" in xml_request:
        #Only apears when verb is GET
        if xml_verb != "GET":
            return "BAD_FORMAT 5000"
        
        #Taking fields
        xml_field = take_substring_from_request(xml_request, "<fields>", "</fields>")

        #If there is any wrong character
        for char in xml_field:
            if not char.isalnum() and char not in [";", " "]:
                return "BAD_FORMAT 5000"

    return "SUCCESS 2000"

    