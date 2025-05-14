import random as r
import socket
import json

class Game:
    def __init__(self):
        s = socket.socket()
        s.bind(("0.0.0.0", 7778))
        s.listen()

        self.IndicesGagnants = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15], #Donne les indices des cases gagnantes
                   [0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],
                   [0,5,10,15],[3,6,9,12]
                    ]
        
        pong = {
        "response": "pong"
        }

        self.jeu = {
            "pos" : None,
            "piece" : None
        }

        pong_data = json.dumps(pong)
        self.jeu_data = json.dumps(self.jeu)

        while True:
            client, addr = s.accept()       # Accepter la connexion
            while True:                     # Boucle de jeu pour le serveur
                reponse = client.recv(4096).decode()
                if not reponse:
                    break

                message = json.loads(reponse)

                if message.get("request") == "ping":  
                    client.sendall(pong_data.encode('utf-8'))
                
                if message.get("request") == "play":    #envoie le message contenant le plateau et la pièce à jouer
                    etat_du_jeu = message.get("state")
                    self.plateau = etat_du_jeu['board']
                    self.piece_a_jouer = etat_du_jeu['piece']
                    print(f"Pièce reçue : {self.piece_a_jouer}")
                    print(message.get("errors"))

                    self.vraie_position = None
                    self.vrai_pion = False
                    
                    self.run()

                    colis = {
                        "response" : "move",
                        "move" : self.jeu,
                        "message" : "Huile de coude 100%"
                    }

                    colis_data = json.dumps(colis)
                    client.sendall(colis_data.encode('utf-8'))

            client.close()

    def give_piece(self):   #Donne la pièce avec caractéristiques les moins présentes sur le plateau
        carac = {"B":0,"S":0,"L":0,"D":0,"F":0,"E":0,"P":0,"C":0}
        for lettre in carac.keys():
            n = 0
            for pion in  self.plateau:
                if pion == None:
                    continue
                if lettre in pion:
                    n += 1
            carac[lettre] = n
        
        minimum_carac = min(carac.values())
        carac_mins = {caract : nombre for caract, nombre in carac.items() if  minimum_carac == nombre}

        Pions_dict = {pion : 0 for pion in self.Pions}

        for lettre in carac_mins:
            for pion in Pions_dict:
                if lettre in pion:
                    Pions_dict[pion] += 1

        maximum_pion = max(Pions_dict, key=Pions_dict.get)
        print(f"Piece à donner : {maximum_pion}")
        self.jeu["piece"] = maximum_pion

    def give_piece_urgence(self, indices): #Si 3 alignées alors urgence de ne pas donner la mauvaise pièce
        pieces_placees = []
        vraie_position = None
        for emplacement in indices:
            pieces_placees.append(self.plateau[emplacement]) #Prend les emplacements rangée par rangée

        n = 0
        for piece in pieces_placees:
            if piece == None:
                n+=1
        
        Dico_carac = {"B":"S", "D":"L", "E":"F", "C":"P", "S":"B", "L":"D", "F":"E", "P":"C"}

        if n == 1 :
            for lettre in "BDECSLFP":
                i = 0
                for piece in pieces_placees:
                    if piece == None:
                        continue
                    if lettre in piece:
                        i += 1

                if i == 3:
                    antidote = Dico_carac[lettre]
                    for pion in self.Pions:
                        if antidote in pion:
                            pion_a_donner = pion
                            self.vrai_pion = True
                            self.jeu["piece"] = pion_a_donner
                            print(f"Pièce à donner urgente : {pion_a_donner}")
                            break
                    break  

    def place(self, position): #Donner la position sur laquelle on place le pion
        if position != None:
            pass
        else:
            Pos_possibles = []
            for numero in range(len(self.plateau)):
                if self.plateau[numero] == None:
                    Pos_possibles.append(numero)
            position = r.choice(Pos_possibles)

        print(f"Position choisie : {position}")

        self.jeu["pos"] = position
    
    def move(self, indices):
        pieces_placees = []
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
                self.vraie_position = indices[position]
                self.place(self.vraie_position)
                break
    
    def run(self):      #Lance le jeu
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

        for piece in self.plateau: #On enlève les pièces déjà placées
            if piece != None:
                pion_trouve = next((p for p in self.Pions if sorted(p) == sorted(piece)), None)
                if pion_trouve:
                        self.Pions.remove(pion_trouve)

        if self.piece_a_jouer != None: #On enlève la pièce à jouer
            pion_trouve = next((p for p in self.Pions if sorted(p) == sorted(self.piece_a_jouer)), None)
            if pion_trouve:
                self.Pions.remove(pion_trouve)

        for liste_indice in self.IndicesGagnants: #On parcourt les indices gagnants
            if self.vraie_position == None and self.piece_a_jouer != None:
                self.move(liste_indice)
            
        if self.vraie_position == None:  
            self.place(None)

        if self.vraie_position == None: #Donne pièce de "contrage"
            for liste_indice in self.IndicesGagnants:
                self.give_piece_urgence(liste_indice)
                if self.vrai_pion == True:
                    break

        if self.vrai_pion == False:
            self.give_piece()

Game()