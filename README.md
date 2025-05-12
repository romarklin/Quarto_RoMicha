# Quarto_RoMicha


## Bibliothèques Utilisées:

Socket : Pour communication avec le serveur
Json : Pour envoyer et decoder les moves reçus et envoyés du serveur
Random : Placer un pion à un endroit aléatoire dans certains cas précis


## Stratégie:

Pour commencer, si plateau vide ou peu fourni, on place aléatoirement les pions.

Dans le cas où on a trois pions alignés avec une caracteristique commune, si on a un pion possèdant cette caracteristique, alors on place le pion 
pour gagner la partie. Si on a pas le pion avec une caracteristique commune on le place aléatoirement et on choisis un pion qui ne possède pas 
cette caracteristique à donner a l'adversaire, pour l'empècher de gagner.

Dans tout les autres cas, le pion est placé de manière aléatoire, mais le pion donné a l'adversaire (et ses caracteristiques) est choisis en fonction du moin de caracteristiques présentes sur le plateau, pour minimiser les chance de donner une oportunité a l'adversaire.


## Matricules

23082 : Mickaël Ba
23138 : Romain Halewyck de Heusch