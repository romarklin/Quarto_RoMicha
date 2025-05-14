# Quarto_RoMicha


## Bibliothèques utilisées:

Socket : Pour communiquer avec le serveur
Json : Pour envoyer et decoder les moves reçus et envoyés au serveur
Random : Placer un pion à un endroit aléatoire dans certains cas précis


## Stratégie:

Pour commencer, si le plateau est vide ou peu fourni, on place les pions aléatoirement.

Dans le cas où l’on a trois pions alignés avec une caractéristique commune, si l’on possède un pion ayant cette caractéristique, on le place pour gagner la partie. Si l’on ne possède pas ce pion, on place un pion aléatoirement et on choisit un pion ne possédant pas cette caractéristique à donner à l’adversaire, pour l’empêcher de gagner.

Dans tous les autres cas, le pion est placé de manière aléatoire, mais le pion donné à l’adversaire (et ses caractéristiques) est choisi en fonction du moindre nombre de caractéristiques déjà présentes sur le plateau, afin de minimiser les chances de lui donner une opportunité.


## Matricules:

23082 : Mickaël Ba
23138 : Romain Halewyck de Heusch