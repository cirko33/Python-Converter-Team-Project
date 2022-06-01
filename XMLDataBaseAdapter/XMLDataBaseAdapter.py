def convertToSQL(xmlText):
    sqlString = "";   

    def find(string):
        startIndex = xmlText.find("<" + string + ">") + len(string) + 2
        endIndex = xmlText.find("</" + string + ">")
        sqlPart = xmlText[startIndex:endIndex]
        return sqlPart
    
    sqlVerb = find("verb")    
    sqlNoun = find("noun")
    sqlFields = find("fields")
    sqlQuery = find("query")
    
    #IF SELECT
    if(sqlVerb == "GET"):
        sqlVerb = "select "
        if(sqlFields == ""):
            sqlFields = "*"
        else:
            sqlFields = sqlFields.replace(";",",")
        sqlNoun = " from " + sqlNoun[1:-2]     
        if(sqlQuery == ""):
            sqlQuery = ""        
        else:
            sqlQuery = " where " + sqlQuery  
            sqlQuery = sqlQuery.replace(";"," and")
        sqlString = sqlVerb + sqlFields + sqlNoun + sqlQuery + ";"
        return sqlString 

    #IF INSERT
    elif(sqlVerb == "POST"):
        sqlField = "" 
        sqlValue = ""       
        sqlVerb = "insert into "
        sqlNoun = sqlNoun[1:-2] + "("
        sqlFields = sqlFields.split(";")
        for temp in sqlFields:          
            sqlField = sqlField + temp.split('=')[0] + "," 
        sqlField = sqlField[0:-1] + (") values(")
        for temp in sqlFields:
            sqlValue = sqlValue + temp.split('=')[1] + "," 
        sqlValue = sqlValue[0:-1] + (")")
        sqlString = sqlVerb + sqlNoun + sqlField + sqlValue + ";"
        return sqlString 

    #IF UPDATE
    elif(sqlVerb == "PATCH"):       
        sqlVerb = "update "
        sqlNoun = sqlNoun[1:-2] + " set "  
        sqlFields = sqlFields.replace(";",",")
        sqlQuery = " where " + sqlQuery  
        sqlQuery = sqlQuery.replace(";"," and")
        sqlString = sqlVerb + sqlNoun + sqlFields + sqlQuery + ";"
        return sqlString 
    
    #IF DELETE
    elif(sqlVerb == "DELETE"): 
        sqlVerb = "delete"
        sqlNoun = " from " + sqlNoun[1:-2]        
        sqlQuery = " where " + sqlQuery  
        sqlQuery = sqlQuery.replace(";"," and")
        sqlString = sqlVerb + sqlNoun + sqlQuery + ";"
        return sqlString

#def convertToXML(text):
    #TODO