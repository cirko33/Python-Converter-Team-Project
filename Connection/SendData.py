import pickle
header_size = 10
def send_data(service, data):
   msg = pickle.dumps(data)
   sending = bytes(f'{len(msg):<{header_size}}', "utf-8") + msg
   service.con.send(sending)

def receive_data(service):
   msg = service.con.recv(2048)
   msglen = int(msg[:header_size])

   while True:
      if len(msg) - header_size == msglen:
         return pickle.loads(msg[header_size:])
      msg += service.con.recv(2048)


