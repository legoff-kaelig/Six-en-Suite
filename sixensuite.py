#############################################################
# Six en Suite                                              #
# Fichier : sixensuite.py                                   #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

from random import shuffle
from suites import *
from multiples import *

couleurs = ["bleu", "rouge", "vert", "jaune", "violet", "orange"]
paquet = []
for i in range(1,13): # La valeur de la Carte
    for j in range(1,7): # La valeur du Dé
        paquet.append((i, j, couleurs[((i + j) - 2) % 6]))
shuffle(paquet) # Mélange du paquet

def init():
    nb_joueurs = int(input("Combien de joueurs participent au jeu ? (1 → 8)"))
    main_joueurs = [ [] for _ in range(nb_joueurs)]
    return nb_joueurs, main_joueurs

# --------------------------------------------------------------------

nb_joueurs, main_joueurs = init()

print(nb_joueurs)