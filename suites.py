#############################################################
# Six en Suite                                              #
# Fichier : suites.py                                       #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

from sixensuite import *
from multiples import *

def is_win(liste):
    """
    Fonction qui renvoie True si la liste passée en paramètre est une suite gagnante, sinon False.
    [[carte, dé, couleur], [carte, dé, couleur], [carte, dé, couleur]]
    """
    if len(liste) < 6:
        return False
    
    for i in range(len(liste)):
