from CheckFormat import *
import sys
sys.path.insert(0, "..")
from Connection.Server import Server

if __name__ == '__main__':
    json_xml_soc = Server(8001)
    xml_db_soc = Server(8002)
    web_client_soc = Server(8000)
    
    while True:
        req = web_client_soc.receive()
        if req.__len__() == 0:
            break
        print("Received request from Web Client and forward to JSONXMLAdapter: " + req )
        json_xml_soc.send(req)

        xml_req = json_xml_soc.receive()
        print("Request in XML form: " + xml_req)

        check = check_xml_format(xml_req)
        if check != "":
            print("Not valid request")
            json_xml_soc.send(check)
            web_client_soc.send(json_xml_soc.receive())
            continue
    
        print("Forward request to XML DB Adapter")
        xml_db_soc.send(xml_req)

        res = xml_db_soc.receive()
        

        print("Forward to JSON XML Adapter")
        json_xml_soc.send(res)

        json_res = json_xml_soc.receive()
        
        print("Forward to Web Client")
        web_client_soc.send(json_res)
    
    web_client_soc.close()
    json_xml_soc.close()
    xml_db_soc.close()