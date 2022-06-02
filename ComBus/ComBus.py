import sys
sys.path.insert(0, "..")
from Connection.Server import Server

s = Server(8000)
while True:
    print("Client: " + s.receive())

    s.send(input("enter text to send"))

    if input("Enter x for exit:") == "x":
        break

s.close()