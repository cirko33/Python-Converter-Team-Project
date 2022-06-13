def convert_to_sql(xml_text):
    sql_string = "";   
    sql_where = " where "

    def find(string):
        start_index = xml_text.find("<" + string + ">") + len(string) + 2
        end_index = xml_text.find("</" + string + ">")
        if(end_index == -1):
            sql_part = ""
        else:            
            sql_part = xml_text[start_index:end_index]        
        return sql_part

    sql_verb = find("verb")    
    sql_noun = find("noun")
    sql_fields = find("fields")
    sql_query = find("query")    

    #Adjust to SQL query
    #IF SELECT
    if(sql_verb == "GET"):
        sql_verb = "select "
        if(sql_fields == ""):
            sql_fields = "*"
        else:
            sql_fields = sql_fields.replace(";",",")
        sql_noun = " from " + sql_noun[1:-2]     
        if(sql_query != ""):
            sql_query = sql_where + sql_query  
            sql_query = sql_query.replace(";"," and")
        sql_string = sql_verb + sql_fields + sql_noun + sql_query + ";"
        return sql_string 

    #IF INSERT
    elif(sql_verb == "POST"):
        sql_field = "" 
        sql_value = ""       
        sql_verb = "insert into "
        sql_noun = sql_noun[1:-2] + "("
        sql_queries = sql_query.split(";")
        for temp in sql_queries:          
            sql_field = sql_field + temp.split('=')[0] + "," 
            sql_value = sql_value + temp.split('=')[1] + ", " 
        sql_field = sql_field[0:-1] + (") values(") 
        sql_value = sql_value[0:-2] + (")")
        sql_string = sql_verb + sql_noun + sql_field + sql_value + ";"
        return sql_string 

    #IF UPDATE
    elif(sql_verb == "PATCH"):       
        sql_verb = "update "
        sql_noun = sql_noun[1:-2] + " set "  
        sql_fields = sql_fields.replace(";",",")
        sql_query = sql_where + sql_query  
        sql_query = sql_query.replace(";"," and")
        sql_string = sql_verb + sql_noun + sql_fields + sql_query + ";"
        return sql_string 
    
    #IF DELETE
    elif(sql_verb == "DELETE"): 
        sql_verb = "delete"
        sql_noun = " from " + sql_noun[1:-2]        
        sql_query = sql_where + sql_query  
        sql_query = sql_query.replace(";"," and")
        sql_string = sql_verb + sql_noun + sql_query + ";"
        return sql_string

def convert_to_xml(text):
    noun,fields,value = text
    xml_answer = "<response>\n"
    if(noun not in ("korisnik","student","profesor")):
        xml_answer += "\t<status>" + noun + "</status>\n"
        xml_answer += "\t<status_code>" + str(fields) + "</status_code>\n"
        xml_answer += "\t<payload>" + value +  "</payload>\n"
        xml_answer += "</response>"
        return xml_answer

    xml_answer += "\t<status>SUCCESS</status>\n"
    xml_answer += "\t<status_code>2000</status_code>\n"        

    if(fields not in ("insert","update","delete")):       
        def get_xml(tuple):            
            xml_a = ""
            if(fields == "*"):
                xml_a += "\t\t\t<id>" + str(tuple[0]) + "</id>\n" 
                xml_a += "\t\t\t<name>" + tuple[1] + "</name>\n" 
                xml_a += "\t\t\t<lastname>" + tuple[2] + "</lastname>\n" 
                xml_a += "\t\t\t<username>" + tuple[3] + "</username>\n" 
                xml_a += "\t\t\t<email>" + tuple[4] + "</email>\n" 
                if(noun == "profesor"):
                    xml_a+= "\t\t\t<department>" + tuple[5] + "</department>\n" 
                elif(noun == "student"):
                    xml_a+= "\t\t\t<year_of_study>" + str(tuple[5]) + "</year_of_study>\n" 
            else:
                field_splitted = fields.split(", ")
                if(len(tuple) != 1):
                    for index in range(len(tuple)):
                        xml_a += "\t\t\t<" + field_splitted[index] + ">" + str(tuple[index]) + "</" + field_splitted[index] + ">\n"
                else:
                    xml_a += "\t\t\t<" + fields + ">" + str(tuple[0]) + "</" + fields + ">\n"
            return xml_a
       
        xml_answer += "\t<payload>\n"
        counter = 0                  
        for tuple in value:                
            xml_answer += "\t\t<" + noun + str(counter) + ">\n"
            xml_answer += get_xml(tuple)
            xml_answer += "\t\t</" + noun + str(counter) + ">\n"
            counter += 1
        
        xml_answer += "\t</payload>\n"
    else:
        xml_answer += "\t<payload>" + str(value) + "</payload>\n"
    
    xml_answer += "</response>"
    return xml_answer

print(convert_to_sql('<request>\n\t<verb>GET</verb>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</request>'))