from pkg_resources import resource_isdir
from RepositoryCommands import send_request
import sys
sys.path.insert(0, "..")
from Connection.Server import Server
from Connection.SendData import send_data

if __name__ == '__main__':
    s = Server(8003)
    while True:
        req = s.receive()
        if len(req) == 0:
            s.close()
            break
        status, status_code, response = send_request(req)
        send_data(s, (status, status_code, response))
        