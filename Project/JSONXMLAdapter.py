from CommunicationBus import CommBus
import json

sviZahtevi = CommBus().sendToJSON()
xmlZahtevi = []
verbCheck = False
nounCheck = False

def ConvertToXML(z):
    
    pocetak = "<request>"
    sredina = ""
    for key,value in z.items():
        sredina += "    <{kljuc}>{vrednost}</{kljuc}>\n".format(kljuc = key, vrednost = value)
    kraj = "</request>"

    xmlString = pocetak + '\n' + sredina + kraj   
    return xmlString

#PROVERA
for zahtev in sviZahtevi:
    verb = zahtev["verb"]
    noun = zahtev["noun"]
    #Verb provera
    if(verb == "GET" or verb == "POST" or verb == "PATCH" or verb == "DELETE"):
        verbCheck = True
    else:
        verbCheck = False
    #Noun provera
    if(noun == "/resurs/1"):        
        nounCheck = True
    else:
        nounCheck = False    
    #DODATI PROVERE ZA FIELDS I QUERY!

    if(verbCheck and nounCheck):
        ret = ConvertToXML(zahtev)
        xmlZahtevi.append(ret)
    #else:
        #print("BAD REQUEST!")
    
#ISPIS
for xmlZahtev in xmlZahtevi:
    print(xmlZahtev + "\n")