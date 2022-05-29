from WebClient import Zahtevi
from JSONXMLAdapter import JSON2XML

class CommBus:
    def __init__(self):
        pass
    
#TEST
listaZahteva = Zahtevi().getAll()
print("Primljeno " + str(len(listaZahteva)) + " zahteva od web clienta!")

for zahtev in listaZahteva:
    xmlZahtev = JSON2XML.ConvertToXML(zahtev)
    print(xmlZahtev)
    print("")