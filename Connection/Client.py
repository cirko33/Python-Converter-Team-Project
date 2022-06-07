import socket

class Client:
    def __init__(self, port):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.connect((socket.gethostname(), port))

    def send(self, message):
        print("Sending: \n" + message)
        self.con.send(message.encode())

    def receive(self):
        ret = self.con.recv(2048).decode()
        print("Received: \n" + ret)
        return ret

    def close(self):
        print("Closing...")
        self.con.close()