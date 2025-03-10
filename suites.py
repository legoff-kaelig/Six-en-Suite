#############################################################
# Six en Suite                                              #
# Fichier : suites.py                                       #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

# from sixensuite import *
# from multiples import *

def is_win(liste):
    """
    Fonction qui renvoie True si la liste passée en paramètre est une suite gagnante, sinon False.
    [(carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur)]

    [(4, 3, 'orange'), (9, 4, 'orange'), (7, 3, 'vert'), (2, 2, 'vert'), (7, 1, 'bleu'), (1, 1, 'bleu'), (1, 3, 'vert'), (8, 5, 'orange'), (11, 1, 'violet'), (2, 6, 'bleu'), (5, 1, 'violet'), (4, 5, 'rouge'), (3, 3, 'violet'), (2, 3, 'jaune'), (6, 2, 'bleu'), (12, 3, 'rouge'), (3, 4, 'orange'), (12, 2, 'bleu'), (5, 5, 'vert'), (5, 4, 'rouge'), (8, 2, 'vert'), (7, 4, 'jaune'), (12, 4, 'vert'), (7, 6, 'orange'), (1, 6, 'orange'), (9, 5, 'bleu'), (6, 4, 'vert'), (4, 4, 'bleu'), (6, 1, 'orange'), (12, 1, 'orange'), (10, 4, 'bleu'), (8, 3, 'jaune'), (5, 3, 'bleu'), (2, 1, 'rouge'), (10, 2, 'violet'), (1, 4, 'jaune'), (9, 2, 'jaune'), (10, 1, 'jaune'), (10, 3, 'orange'), (8, 6, 'bleu'), (2, 4, 'violet'), (1, 5, 'violet'), (9, 3, 'violet'), (2, 5, 'orange'), (10, 6, 'vert'), (10, 5, 'rouge'), (11, 3, 'bleu'), (6, 6, 'violet'), (11, 6, 'jaune'), (5, 2, 'orange'), (6, 5, 'jaune'), (7, 2, 'rouge'), (11, 2, 'orange'), (9, 6, 'rouge'), (4, 6, 'vert'), (8, 4, 'violet'), (11, 5, 'vert'), (6, 3, 'rouge'), (3, 6, 'rouge'), (4, 1, 'jaune'), (11, 4, 'rouge'), (12, 5, 'jaune'), (3, 2, 'jaune'), (3, 1, 'vert'), (5, 6, 'jaune'), (7, 5, 'violet'), (12, 6, 'violet'), (1, 2, 'rouge'), (3, 5, 'bleu'), (4, 2, 'violet'), (8, 1, 'rouge'), (9, 1, 'vert')]

    """
    if len(liste) < 6:
        return False
    
    for i in range(len(liste)-1):
        for j in range(len(liste[i])):
            if liste[i][j] == liste[i+1][j]:
                x =+ 1
                if x >= 5:
                    return True
    return False
                
print(is_win([(4, 4, 'orange'), (4, 4, 'orange'), (4, 4, 'orange'), (4, 4, 'orange'), (4, 4, 'orange'), (4, 4, 'orange')]))