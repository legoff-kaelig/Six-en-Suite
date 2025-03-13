#############################################################
# Six en Suite                                              #
# Fichier : suites.py                                       #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

COULEURS = ["bleu", "rouge", "vert", "jaune", "violet", "orange"]

def is_win(liste):
    """
    Fonction qui renvoie True si la liste passée en paramètre est une suite gagnante, sinon False.
    [(carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur)]

    Ex de suite envoyé : [(4, 3, 'orange'), (9, 4, 'orange'), (7, 3, 'vert')]

    """
    x = 0
    
    if len(liste) < 6:
        return False

    couleur = [carte[2] for carte in liste]
    valeurs = [carte[0] for carte in liste]
    
    # 6 même couleurs
    for i in couleur:  
        if couleur.count(i) >= 6:
            return True

    # 6 même valeurs
    for x in valeurs:  
        if valeurs.count(x) >= 6:
            return True

    # Toutes les couleurs





    return False

        
print(is_win([(4, 3, 'orange'), (5, 4, 'orange'), (7, 3, 'orange'), (4, 2, 'vert'), (8, 1, 'vert'), (4, 1, 'vert'), (7, 1, 'vert'), (7, 1, 'vert')]))