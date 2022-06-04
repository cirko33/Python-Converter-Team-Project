import random
import time

requests = []
querys = ['"name = \'Luka\'"', '"username = \'jelovopopov\'"', '"department = \'EEPSI\'"', '"name = \'Dejan\' and year_of_study = \'3\'"', '"department = \'ACS\' and name = \'Petar\'"', '"username = \'dekikuki\'"']
fields = ['"*"', '"id; name; email"', '"id; name; lastname;"', '"id; username;"', '"name; lastname; department"', '"name; lastname; year_of_study;"']
nouns = ['"/korisnik/1"', '"/student/1"', "/profesor/1"]

for i in range(10):
    requests.append('{ "verb" : "GET", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ', "fields" : '  + random.choice(fields) + ' }')
for i in range(10):
    requests.append('{ "verb" : "DELETE", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ' }')
for i in range(10):
    requests.append('{ "verb" : "PATCH", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ', "fields" : '  + random.choice(fields) + ' }')

requests.append('{ "verb" : "POST", "noun" : /student/1, "query" : "id = \'10\'; name = \'Maja\'; lastname = \'Vucurevic\'; username = \'vuca01\'; year_of_study = \'2\'" }')
requests.append('{ "verb" : "POST", "noun" : /korisnik/1, "query" : "id = \'12\'; name = \'Marko\'; lastname = \'Markovic\'; username = \'marecare\'; email = \'markomarko@gmail.com\'" }')
requests.append('{ "verb" : "POST", "noun" : /profesor/1, "query" : "id = \'13\'; name = \'Dragan\'; lastname = \'Ivetic\'; username = \'ivetic\'; email = \'ivetic@uns.ac.rs\'; department = \'ESI\'" }')
requests.append('{ "verb" : "POST", "noun" : /korisnik/1, "query" : "id = \'3\'; name = \'Lazar\'; lastname = \'Lazarevic\'; username = \'ludilaza\'; email = \'lazalaza@gmail.com\'" }')
requests.append('{ "verb" : "POST", "noun" : /profesor/1, "query" : "id = \'2\'; name = \'Mirko\'; lastname = \'Mirkovic\'; username = \'mirskosvirko\'; email = \'mirkovic@uns.ac.rs\'; department = \'ACS\'" }')
requests.append('{ "verb" : "GET", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ' }')
requests.append('{ "verb" : "DELETE", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ' "fields" : "id; name; lastname;" }')
requests.append('{ "verb" : "DELETE", "noun" : ' + random.choice(nouns) + ', "query" : ' + random.choice(querys) + ' "fields" : "id; username;" }')
requests.append('{ "verb" : "GET", "noun" : ' + random.choice(nouns) + ', "fields" : "name; username;" }')

for i in range(50):
    print(random.choice(requests))
    time.sleep(1)