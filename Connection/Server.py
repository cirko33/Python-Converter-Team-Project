import socket

class Server:
    def __init__(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), port))
        self.s.listen(1)
        self.con, self.add = self.s.accept()
        print("Connected with: " + str(self.add))


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