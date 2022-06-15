import sys, time, keyboard
from Requests import request
sys.path.insert(0, "..")
from Connection.Client import Client

if __name__ == '__main__':
    c = Client(8000)
    active = True
    while active:
        c.send(request())

        ret = c.receive()

        print("Press x for exit:")
        for i in range(50):
            if keyboard.is_pressed("x"):
                c.close()
                active = False
                break
            time.sleep(0.1)