from WebClient import Zahtevi

class CommBus:
    def __init__(self):
        pass

    def sendToJSON(self): #posalji zahteve na JSONXMLConverter        
        return listaZahteva

#TEST
listaZahteva = Zahtevi().getAll()
print("Primljeno " + str(len(listaZahteva)) + " zahteva od web clienta!")