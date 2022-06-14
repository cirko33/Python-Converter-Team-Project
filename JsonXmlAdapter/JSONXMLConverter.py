import json, xmltodict

def convert_to_json(text):
    xmldict = xmltodict.parse(text)
    ret = json.dumps(xmldict)
    return ret[ret.find(':') + 2 : -1]
    
def convert_to_xml(text):
    zahtev = json.loads(text)        
    ret = "<request>\n"
    for key,value in zahtev.items():
        ret += "\t<{kljuc}>{vrednost}</{kljuc}>\n".format(kljuc = key, vrednost = value)  
    ret += "</request>"     
    return ret 
