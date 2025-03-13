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

    couleur = [carte[2] for carte in liste]
    valeurs = [carte[0] for carte in liste]
    
    # Vérification des couleurs
    nb_couleur = 0
    for i in couleur:
        nb_couleur = COULEURS.count(i)
        
        if nb_couleur >= 6:
            return True
        
    # Vérification des valeurs
    nb_cartes = 0
    for x in valeurs:
        nb_cartes = valeurs.count(x)
        if nb_cartes >= 6:
            return True
        
print(is_win([(4, 3, 'orange'), (5, 4, 'vert'), (4, 3, 'vert'), (4, 2, 'vert'), (4, 1, 'vert'), (4, 1, 'vert'), (7, 1, 'vert'), (7, 1, 'vert')]))