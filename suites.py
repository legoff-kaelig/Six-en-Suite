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
    Format d'une liste de 6 cartes ou plus : [(carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur)]

    """
    if len(liste) < 6:
        return False

    color = [carte[2] for carte in liste]
    val = [carte[0] for carte in liste]

    # 6 même couleurs
    for i in color:  
        if color.count(i) >= 6:
            return True


    # 6 même valeurs
    for j in val:  
        if val.count(j) >= 6:
            return True


    # 6 de chaques couleurs
    color_count = [0] * len(COULEURS)

    for count in color:
        color_count[COULEURS.index(count)] += 1

    for k in color_count:
        if k == 0:
            return False

    return True



        
def test_suites():
    """
    Fonction de test pour vérifier les différentes conditions de victoire dans le jeu Six en Suite.
    Cette fonction utilise des assertions pour vérifier que la fonction is_win() retourne les résultats attendus
    pour différentes configurations de cartes.
    """
    # 6 cartes de la même couleur
    assert is_win([(1, 3, 'bleu'), (2, 4, 'bleu'), (3, 3, 'bleu'), (4, 2, 'bleu'), (5, 1, 'bleu'), (6, 1, 'bleu')]) == True
    assert is_win([(9, 2, 'rouge'), (10, 3, 'rouge'), (11, 5, 'rouge'), (12, 1, 'rouge'), (13, 4, 'rouge'), (14, 6, 'rouge')]) == True

    # 6 cartes avec la même valeur
    assert is_win([(4, 3, 'bleu'), (4, 4, 'rouge'), (4, 3, 'vert'), (4, 2, 'jaune'), (4, 1, 'violet'), (4, 1, 'orange')]) == True
    assert is_win([(7, 5, 'bleu'), (7, 6, 'rouge'), (7, 1, 'vert'), (7, 3, 'jaune'), (7, 2, 'violet'), (7, 4, 'orange')]) == True

    # Une carte de chaque couleur (exactement 6 couleurs différentes)
    assert is_win([(1, 3, 'bleu'), (2, 4, 'rouge'), (3, 3, 'vert'), (4, 2, 'jaune'), (5, 1, 'violet'), (6, 1, 'orange')]) == True
    assert is_win([(10, 6, 'bleu'), (11, 2, 'rouge'), (12, 5, 'vert'), (13, 4, 'jaune'), (14, 3, 'violet'), (15, 1, 'orange')]) == True

    # Moins de 6 cartes → Doit toujours être False
    assert is_win([(1, 3, 'bleu'), (2, 4, 'rouge'), (3, 3, 'vert'), (4, 2, 'jaune'), (5, 1, 'violet')]) == False
    assert is_win([(7, 3, 'orange'), (8, 4, 'orange'), (9, 2, 'vert'), (10, 6, 'rouge'), (11, 1, 'jaune')]) == False

    # Mélange qui ne correspond à aucun cas gagnant
    assert is_win([(1, 3, 'bleu'), (2, 4, 'rouge'), (3, 3, 'bleu'), (4, 2, 'vert'), (5, 1, 'jaune'), (6, 1, 'jaune')]) == False
    assert is_win([(9, 5, 'violet'), (10, 3, 'orange'), (11, 2, 'rouge'), (12, 4, 'bleu'), (13, 1, 'jaune'), (14, 6, 'jaune')]) == False

    # Plus de 6 cartes, mais aucune condition remplie
    assert is_win([(1, 3, 'bleu'), (2, 4, 'rouge'), (3, 3, 'vert'), (4, 2, 'jaune'), (5, 1, 'violet'), (6, 1, 'orange'), (7, 2, 'bleu')]) == False
    assert is_win([(8, 6, 'violet'), (9, 3, 'orange'), (10, 4, 'rouge'), (11, 5, 'bleu'), (12, 1, 'jaune'), (13, 2, 'vert'), (14, 6, 'rouge')]) == False

    # 6 cartes mais avec une couleur manquante
    assert is_win([(1, 3, 'bleu'), (2, 4, 'rouge'), (3, 3, 'vert'), (4, 2, 'jaune'), (5, 1, 'violet'), (6, 1, 'violet')]) == False
    assert is_win([(7, 3, 'bleu'), (8, 5, 'rouge'), (9, 1, 'vert'), (10, 2, 'jaune'), (11, 4, 'violet'), (12, 6, 'violet')]) == False