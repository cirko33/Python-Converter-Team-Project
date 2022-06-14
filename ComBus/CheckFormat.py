

def check_xml_format(xml_request):
    #Required fields
    if "verb" not in xml_request or "noun" not in xml_request:
        return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Verb and noun are required</payload></response>"

    def take_substring_from_request(request, begin_string, end_string):
        begin = request.find(begin_string) + len(begin_string)
        end = request.find(end_string)

        substring = request[begin : end]

        return substring

    #Taking value of verb
    xml_verb = take_substring_from_request(xml_request, "<verb>", "</verb>")

    #Cheking value of verb
    if xml_verb not in ["GET", "POST", "DELETE", "PATCH"]:
        return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Verb not valid</payload></response>"

    #Optional field
    if "query" in xml_request:
        #Taking value of query
        xml_query = take_substring_from_request(xml_request, "<query>", "</query>")

        #If there is any invalid character
        for char in xml_query:
            if not char.isalnum() and char not in [";", "=", "'", " ", "_", "@", "."]:
                return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid characters in query</payload></response>"

        #Does every query have '=' 
        queries = xml_query.split(";")
        for query in queries:
            if "=" not in query:
                return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Missing '=' in query</payload></response>"
    else:
        if xml_verb == "POST":
            return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Query is required for POST verb</payload></response>"
    #Optional field
    if "fields" in xml_request:
        #Only apears when verb is GET
        if xml_verb == "DELETE":
            return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>DELETE can't have fields</payload></response>"

        #Taking fields
        xml_field = take_substring_from_request(xml_request, "<fields>", "</fields>")

        if xml_verb == "PATCH":
            for char in xml_field:
                if not char.isalnum() and char not in [";", "=", "'", " ", "_", "@", "."]:
                    return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid character in patch fields</payload></response>"

            #Does every patch_field have '=' 
            fields = xml_field.split(";")
            for field in fields:
                if "=" not in field:
                    return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Missing '=' in patch fields</payload></response>"
        else:
            #If there is any wrong character
            for char in xml_field:
                if not char.isalnum() and char not in [";", " ", "_", "*"]:
                    return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid character in fields</payload></response>"
    else:
        if xml_verb == "PATCH":
            return "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Fields are required for PATCH verb</payload></response>"
    return ""