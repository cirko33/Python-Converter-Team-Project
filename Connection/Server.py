from socket import *
class Server:
    def __init__(self, port):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((gethostname(), port))
        self.s.listen()
        self.accept()

    def accept(self):
        self.con, self.add = self.s.accept()
        print("Connected with: " + str(self.add))

    def send(self, message):
        try:
            self.con.send(message.encode())
        except:
            self.close()
            self.accept()
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
            self.accept()
            return self.receive()

        print("Received: \n" + ret)
        return ret

    def close(self):
        self.con.close()
