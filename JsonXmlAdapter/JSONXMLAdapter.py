import json, xmltodict

def convert_to_json(text):
    xmldict = xmltodict.parse(text)
    return json.dumps(xmldict)[13:-1]
    
def convert_to_xml(z):
    zahtev = json.loads(z)        
    ret = "<request>\n"
    for key,value in zahtev.items():
        ret += "\t<{kljuc}>{vrednost}</{kljuc}>\n".format(kljuc = key, vrednost = value)  
    ret += "</request>"     
    return ret 
