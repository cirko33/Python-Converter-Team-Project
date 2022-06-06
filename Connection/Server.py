import socket

class Server:
    def __init__(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), port))
        self.s.listen(1)
        self.con, self.add = self.s.accept()


    def send(self, message):
        self.con.send(message.encode())

    def receive(self):
        return self.con.recv(2048).decode()

    def close(self):
        self.con.close()