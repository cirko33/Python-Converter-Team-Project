import json

class Zahtevi:
    def __init__(self):      
        pass  

    def getAll(self):
        return sviZahtevi

zahtev0 ={
    "verb": "GET",
    "noun": "/resurs/1",
    "query": "name='pera'; type=1",
    "fields": "id; name; surname"
}

zahtev1 ={
    "verb": "POST",
    "noun": "/resurs/1",
    "query": "name='zika'; type=1",
    "fields": "id; name"
}

zahtev2 ={
    "verb": "PATCH",
    "noun": "/resurs/1",
    "query": "name='pera'; type=1",
    "fields": "id; surname"
}

zahtev3 ={
    "verb": "DELETE",
    "noun": "/resurs/1",
    "query": "name='pera'; type=1",
    "fields": "id; name; surname"
}

zahtev4 ={
    "verb": "CREATE",
    "noun": "/resurs/1",
    "query": "name='pera'; surname='peric'; type=1",
    "fields": "id; name; surname"
}

sviZahtevi = [zahtev0,zahtev1,zahtev2,zahtev3,zahtev4]