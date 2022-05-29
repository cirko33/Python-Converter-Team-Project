import json, xmltodict

class JSON2XML:
    def ConvertToJSON(text):
        xmldict = xmltodict.parse(text)
        return json.dumps(xmldict)
        
    def ConvertToXML(zahtev):
        verb = zahtev["verb"]
        noun = zahtev["noun"]
        if(verb not in("GET","POST","PATCH","DELETE")):
            return #(False, BAD_REQUEST, ####)
        if(noun != "/resurs/1"):
            return #(False, BAD_REQUEST, ####)
        #DODATI PROVERE ZA FIELDS I QUERY POLJA
        
        pocetak = "<request>"
        sredina = ""
        for key,value in zahtev.items():
            sredina += "    <{kljuc}>{vrednost}</{kljuc}>\n".format(kljuc = key, vrednost = value)
        kraj = "</request>"

        xmlString = pocetak + '\n' + sredina + kraj           
        return xmlString #(True, xmlString, ####)
