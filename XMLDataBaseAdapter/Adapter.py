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

        sql_req = convert_to_sql(req)

        rep.send(sql_req)

        res = receive_data(rep)

        xml_res = convert_to_xml(res)

        combus.send(xml_res)
    
    combus.close()
    rep.close()