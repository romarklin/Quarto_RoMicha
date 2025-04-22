import math
import socket
import json
import os

class Game:
    def __init__(self):
        """s = socket.socket()
        s.bind(("127.0.0.1", 8887))
        s.listen()"""

        Pions = {
           "SLEP",
           "SDEP",
           "SLEC",
           "BDEC",
           "SLFP",
           "SLFC",
           "BDFP",
           "SDFP",
           "SDFC",
           "BLFP",
           "SDEC",
           "BLEP",
           "BDEP",
           "BLFC",
           "BLEC",
           "BDFC"
        }

        self.IndicesGagnants = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],
                   [0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],
                   [0,5,10,15],[3,6,9,12]
                    ]
        
        with open('test.json','r') as file:
            test = json.load(file)

        pong = {
        "response": "pong"
        }
        pong_data = json.dumps(pong)

        """while True:
            client, addr = s.accept()
            while True:
                reponse = client.recv(4096).decode()
                if not reponse:
                    break

                message = json.loads(reponse)

                if message.get("request") == "ping":
                    client.sendall(pong_data.encode('utf-8'))
                
                if message.get("request") == "play":
                    etat_du_jeu = message.get("state")

            client.close()"""
        
        self.plateau = test['board']
        self.piece_a_jouer = test['piece']
    
    def move(self, indices):
        pieces_placees = []
        for emplacement in indices:
            pieces_placees.append(self.plateau[emplacement])

        for lettre in "BDECSLFP":
            if lettre not in self.piece_a_jouer:
                continue
            n = 0
            vide = False
            for piece in pieces_placees:
                if piece == None:
                    vide = True
                    continue
                if lettre in piece:
                    n += 1
            
            if n == 3 and vide == True:
                #placer la piece
                break
    
    def run(self):
        for liste_indice in self.IndicesGagnants:
            self.move(liste_indice)

Game().run()