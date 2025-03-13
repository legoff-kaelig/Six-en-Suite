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

    color = [carte[2] for carte in liste]
    val = [carte[0] for carte in liste]
    
    # 6 même couleurs
    for i in color:  
        if color.count(i) >= 6:
            return True


    # 6 même valeurs
    for x in val:  
        if val.count(x) >= 6:
            return True


    # 6 de chaques couleurs
    color_count = [0] * len(COULEURS)

    for count in color:
        if color.count(count) == 0:
            return False
        color_count[COULEURS.index(count)] += 1

    for i in color_count:
        if i == 0:
            return False

    return True

        
print(is_win([(4, 3, 'bleu'), (5, 4, 'rouge'), (7, 3, 'vert'), (4, 2, 'jaune'), (8, 1, 'violet'), (4, 1, 'orange'), (7, 1, 'vert'), (7, 1, 'vert')]))