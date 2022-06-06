import socket

class Client:
    def __init__(self, port):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.connect((socket.gethostname(), port))

    def send(self, message):
        self.con.send(message.encode())

    def receive(self):
        return self.con.recv(2048).decode()

    def close(self):
        self.con.close()