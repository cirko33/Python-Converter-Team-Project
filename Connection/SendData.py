import pickle

def send_data(service, data):
   service.con.send(pickle.dumps(data))

def receive_data(service):
    return pickle.loads(service.con.recv(2048))