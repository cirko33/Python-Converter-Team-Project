from JSONXMLConverter import convert_to_json, convert_to_xml
import sys
sys.path.insert(0, "..")

from Connection.Client import Client

if __name__ == "__main__":
    c = Client(8001)
    
    while True:
        pack = c.receive()
        
        if pack.startswith('<'):
            print("Converting to JSON")
            ret = convert_to_json(pack)
        else:
            print("Converting to XML")
            ret = convert_to_xml(pack)

        c.send(ret)
    