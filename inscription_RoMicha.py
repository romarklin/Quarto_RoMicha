import socket
import json

s = socket.socket()
s.connect(("localhost", 3000))

requete = {
  "request": "subscribe",
  "port": 8885,
  "name": "MDR",
  "matricules": ["23023", "22134"]
}

requete_data = json.dumps(requete)

s.sendall(requete_data.encode('utf-8'))

reponse = s.recv(4096)
print(reponse.decode())

s.close()