#############################################################
# Six en Suite                                              #
# Fichier : suites.py                                       #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

#import sixensuite
# from multiples import *
COULEURS = ["bleu", "rouge", "vert", "jaune", "violet", "orange"]

def is_win(liste):
    """
    Fonction qui renvoie True si la liste passée en paramètre est une suite gagnante, sinon False.
    [(carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur)]

    Ex de suite envoyé : [(4, 3, 'orange'), (9, 4, 'orange'), (...), (7, 3, 'vert')]

    """
    x = 0
    
    if len(liste) < 6:
        return False
    
    # for i in range(len(liste)-1):
    #     for j in range(len(liste[i])):
    #         if liste[i][j] == liste[i+1][j]:
    #             x += 1
    #             if x >= 5:
    #                 return True
    # return False

    couleur = [carte[2] for carte in liste]
    valeurs = [carte[0] for carte in liste]
    
    # Vérification des couleurs
    nb_couleur = 0
    for i in couleur:
        nb_couleur = COULEURS.count(couleur[i])
        
        if nb_couleur >= 6:
            return True
        else:
            return False
        

print(is_win([(4, 3, 'orange'), (4, 4, 'vert'), (4, 3, 'orange'), (4, 2, 'orange'), (1, 1, 'vert'), (7, 1, 'orange'), (7, 1, 'orange'), (7, 1, 'orange')]))