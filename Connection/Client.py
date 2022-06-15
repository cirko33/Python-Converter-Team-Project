import time
from socket import *

class Client:
    def __init__(self, port):
        self.con = socket(AF_INET, SOCK_STREAM)
        self.port = port
        self.connect()

    def connect(self):
        while True:
            try:
                self.con = socket(AF_INET, SOCK_STREAM)
                self.con.connect((gethostname(), self.port))
                break
            except:
                time.sleep(1)

    def send(self, message):
        try:
            self.con.send(message.encode())
        except:
            self.close()
            self.connect()
            self.send(message)
            return

        print("Sending: \n" + message)

    def receive(self):
        try:
            ret = self.con.recv(2048).decode()
        except:
            ret = ""
        
        if len(ret) == 0:
            self.close()
            self.connect()
            return self.receive()

        print("Received: \n" + ret)
        return ret

    def close(self):
        self.con.shutdown(SHUT_RDWR)
        self.con.close()
