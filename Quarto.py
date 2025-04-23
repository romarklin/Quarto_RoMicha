import math
import socket
import json
import os

class Game:
    def __init__(self):
        """s = socket.socket()
        s.bind(("127.0.0.1", 8887))
        s.listen()"""

        self.Pions = {
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

        for piece in self.plateau:
            if piece != None:
                self.Pions.remove(piece)

        print(self.Pions)

    def give_piece(self):
        carac = {"B":0,"S":0,"L":0,"D":0,"F":0,"E":0,"P":0,"C":0}
        for lettre in carac.keys():
            n = 0
            for pion in  self.plateau:
                if pion == None:
                    continue
                if lettre in pion:
                    n += 1
            carac[lettre] = n

    def place(self, vraie_position): #Donner la position sur laquelle on place le pion
        if vraie_position != None:
            print(vraie_position)
        else:
            l = 1
    
    def move(self, indices):
        pieces_placees = []
        vraie_position = None
        for emplacement in indices:
            pieces_placees.append(self.plateau[emplacement]) #Prend les emplacements rangée par rangée

        for lettre in "BDECSLFP":
            if lettre not in self.piece_a_jouer: #Identification des caractéristiques communes
                continue
            n = 0
            i = 0
            vide = False
            for piece in pieces_placees:
                if piece == None:
                    vide = True
                    position = i
                    continue
                if lettre in piece:
                    n += 1
                i += 1
            
            if n == 3 and vide == True: #Placer la pièce gagnante
                vraie_position = indices[position]
                print(vraie_position)
                break
        
            self.place(vraie_position)

    
    def run(self):
        for liste_indice in self.IndicesGagnants:
            self.move(liste_indice)
        self.give_piece()

Game().run()