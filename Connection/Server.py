import socket

class Server:
    def __init__(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind("localhost", port)
        self.s.listen(1)
        self.con = self.s.accept()


    def send(self, message):
        self.con.send(message)

    def receive(self):
        return self.con.recv(256)

    def close(self):
        self.con.close()