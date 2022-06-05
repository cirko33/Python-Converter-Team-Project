import sys, random, time
from Requests import *
sys.path.insert(0, "..")
from Connection.Client import Client

c = Client(8000)
while 3:
    time.sleep(5)
    c.send(requests[random.randint(0, requests.count() - 1)])

    print("Server: " + c.receive())
    if input("Enter x for exit:") == "x":
        c.close()
        break

