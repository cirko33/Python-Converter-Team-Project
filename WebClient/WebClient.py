import sys
sys.path.insert(0, "..")
from Connection.Client import Client

c = Client(8000)
while True:
    c.send(input("enter text to send"))

    print("Server: " + c.receive())
    if input("Enter x for exit:") == "x":
        break

