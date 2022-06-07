import sys, time
from Requests import *
sys.path.insert(0, "..")
from Connection.Client import Client

if __name__ == '__main__':
    c = Client(8000)

    while True:
        time.sleep(3)
        c.send(request())

        ret = c.receive()
        if len(ret) == 0:
            c.close()
            break

        if input("Enter x for exit:") == "x":
            c.close()
            break

