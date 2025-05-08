import socket
import json

s = socket.socket()
s.connect(("172.17.10.133", 3000))

requete = {
  "request": "subscribe",
  "port": 8885,
  "name": "RoMicha",
  "matricules": ["23082", "23138"]
}

requete_data = json.dumps(requete)

s.sendall(requete_data.encode('utf-8'))

reponse = s.recv(4096)
print(reponse.decode())

s.close()