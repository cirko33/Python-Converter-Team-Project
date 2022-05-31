def convertToSQL(xmlText):
    sqlString = "";   

    #FINDING VERB
    startIndex = xmlText.find("<verb>") + len("<verb>")
    endIndex = xmlText.find("</verb>")
    sqlVerb = xmlText[startIndex:endIndex]

    #FINDING NOUN
    startIndex = xmlText.find("<noun>") + len("<noun>")
    endIndex = xmlText.find("</noun>")
    sqlNoun = xmlText[startIndex:endIndex]   

    #FINDING QUERY
    if("<query>" not in xmlText):
        sqlQuery = ""
    else:
        startIndex = xmlText.find("<query>") + len("<query>")
        endIndex = xmlText.find("</query>")
        sqlQuery = xmlText[startIndex:endIndex]  

    #FINDING FIELDS     
    if("<fields>" not in xmlText):
        sqlFields = ""
    else:
        startIndex = xmlText.find("<fields>") + len("<fields>")
        endIndex = xmlText.find("</fields>")
        sqlFields = xmlText[startIndex:endIndex]  

    #Adjust to SQL query
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