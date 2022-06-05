from XMLDataBaseConverter import *
import sys
sys.path.insert(0, "..")
from Connection.Client import Client
from Connection.SendData import receive_data

if __name__ == '__main__':
    combus = Client(8002)
    rep = Client(8003)
    while True:
        req = combus.receive()
        if req.__len__() == 0:
            break
        print("Received from ComBus: " + req)

        sql_req = convert_to_sql(req)
        print("Request in SQL form: " + sql_req)

        print("Forwarding to Repository")
        rep.send(sql_req)

        res = receive_data(rep)
        print("Received response from Repository: " + res)

        xml_res = convert_to_xml(res)
        print("Response in XML form: " + xml_res)
        
        print("Forward to ComBus")
        combus.send(xml_res)
    
    combus.close()
    rep.close()