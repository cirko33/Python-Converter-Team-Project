from CheckFormat import *
import sys
sys.path.insert(0, "..")
from Connection.Server import Server

if __name__ == '__main__':
    web_client_soc = Server(8000)
    json_xml_soc = Server(8001)
    xml_db_soc = Server(8002)

    while True:
        req = web_client_soc.receive()
        print("Received request from Web Client and forward to JSONXMLAdapter: " + req )
        json_xml_soc.send(req)

        xml_req = json_xml_soc.receive()
        print("Request in XML form: " + xml_req)

        check = check_xml_format(xml_req)
        if check != "SUCCESS 2000":
            print("Not valid request")
            web_client_soc.send(check)
            continue
        
        print("Forward request to XML DB Adapter")
        xml_db_soc.send(xml_req)

        res = xml_db_soc.receive()
        print("Received response from XML DB Adapter: " + res)

        print("Forward to JSON XML Adapter")
        json_xml_soc.send(res)

        json_res = json_xml_soc.receive()
        print("Received response from JSON XML Adapter: " + json_res)
        
        print("Forward to Web Client")
        web_client_soc.send(json_res)
    
    web_client_soc.close()
    json_xml_soc.close()
    xml_db_soc.close()