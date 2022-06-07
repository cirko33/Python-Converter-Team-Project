import pickle
header_size = 10
def send_data(service, data):
   print("Sending: " + str(data))
   msg = pickle.dumps(data)
   sending = bytes(f'{len(msg):<{header_size}}', "utf-8") + msg
   service.con.send(sending)

def receive_data(service):
      msg = service.con.recv(2048)
      msglen = int(msg[:header_size])
      while True:
         if len(msg) - header_size == msglen:
            ret = pickle.loads(msg[header_size:])
            print("Received: " + str(ret))
            return ret

         msg += service.con.recv(2048)
   

