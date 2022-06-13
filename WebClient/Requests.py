import random

verbs = ['"GET"', '"POST"', '"PATCH"', '"DELETE"']
nouns = ['"/korisnik/1"', '"/student/1"', '"/profesor/1"']
queries = ['"name = \'Luka\'"', '"username = \'jelovopopov\'"', '"username = \'dekikuki\'"', '"name = \'Petar\'"', '"year_of_study = 3; name = \'Dejan\'"', '"department = \'EEPSI\'"']
fields = ['"*"', '"id; name; email"', '"id; name; lastname"', '"id; username"', '"name; lastname; department"', '"name; lastname; year_of_study"']

def request():
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    if verb != '"POST"':
        if "korisnik" in noun:
            query = random.choice(queries[:4])    
        else:
            query = random.choice(queries)
    else:
        if noun == '"/korisnik/1"':
            query = '"id = \'12\'; name = \'Marko\'; lastname = \'Markovic\'; username = \'marecare\'; email = \'markomarko@gmail.com\'"'
        elif noun == '"/student/1"':
            query = '"id = 10; name = \'Maja\'; lastname = \'Vucurevic\'; username = \'vuca01\'; year_of_study = 2"'
        else:
            query = '"id = 13; name = \'Dragan\'; lastname = \'Ivetic\'; username = \'ivetic\'; email = \'ivetic@uns.ac.rs\'; department = \'ESI\'"'

    if verb == '"GET"':
        if "korisnik" in noun:
            field = random.choice(fields[:4])
        else:
            field = random.choice(fields)
    elif verb == '"PATCH"':
        if "korisnik" in noun:
            field = random.choice(queries[:4])
        else:
            field = random.choice(queries)
    else:
        field = ""
    
    verb = f'"verb" : {verb}'
    noun = f', "noun" : {noun}'
    query = f', "query" : {query}'
    if field != "":
        field = f', "fields" : {field}'

    return "{ " + verb + noun + query + field + " }"