#############################################################
# Six en Suite                                              #
# Fichier : suites.py                                       #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

COULEURS = ["bleu", "rouge", "vert", "jaune", "violet", "orange"]

def is_win(liste):
    """
    Fonction qui renvoie True si la liste passée en paramètre représente une suite gagnante, sinon False.
    Exemple de format d'une liste de 3 cartes : [(carte, dé, couleur), (carte, dé, couleur), (carte, dé, couleur)]

    Input:
    liste (list): Une liste de tuples, où chaque tuple représente une carte avec sa valeur, sa valeur de dé, et sa couleur.

    Output:
    bool: True si la liste représente une suite gagnante, False sinon.
    """
    # Si la liste a moins de 6 cartes, pas de combinaison possible
    if len(liste) < 6:
        return False

    color = [carte[2] for carte in liste]

    # Condition 1 : Vérifie s'il existe une couleur avec 6+ occurrences
    for i in color:  
        if color.count(i) >= 6:
            return True


    # Condition 2 : Vérifie la présence d'au moins une carte de chaque couleur
    color_count = [0] * len(COULEURS)

    for count in color:
        color_count[COULEURS.index(count)] += 1

    for k in color_count:
        if k == 0:
            return False

    return True


def test_suites():
    """
    Fonction de test pour vérifier les différentes conditions de victoire.
    Vérifie is_win(), ne retourne :
        - rien, si pas d'erreur
        - crash s'il y en a une
    """
    # Cas perdant : moins de 6 cartes
    assert is_win([(1, 2, "bleu"), (3, 4, "rouge"), (5, 6, "vert")]) == False
    assert is_win([(2, 3, "jaune"), (4, 5, "violet"), (6, 1, "orange"), (1, 4, "rouge")]) == False

    # Cas perdant : pas 6 cartes de la même couleur
    assert is_win([(1, 2, "bleu"), (3, 4, "rouge"), (5, 6, "vert"), (2, 3, "jaune"), (4, 5, "violet"), (6, 1, "rouge")]) == False
    assert is_win([(2, 3, "vert"), (4, 5, "vert"), (6, 1, "vert"), (1, 2, "vert"), (3, 4, "jaune"), (5, 6, "orange"), (2, 5, "bleu")]) == False

    # Cas gagnant : 6 cartes de la même couleur
    assert is_win([(1, 2, "bleu"), (3, 4, "bleu"), (5, 6, "bleu"), (2, 3, "bleu"), (4, 5, "bleu"), (6, 1, "bleu")]) == True
    assert is_win([(2, 3, "rouge"), (4, 5, "rouge"), (6, 1, "rouge"), (1, 2, "rouge"), (3, 4, "rouge"), (5, 6, "rouge"), (2, 5, "rouge")]) == True

    # Cas gagnant : 6 couleurs différentes
    assert is_win([(1, 2, "bleu"), (3, 4, "rouge"), (5, 6, "vert"), (2, 3, "jaune"), (4, 5, "violet"), (6, 1, "orange")]) == True
    assert is_win([(2, 3, "jaune"), (4, 5, "violet"), (6, 1, "orange"), (1, 2, "bleu"), (3, 4, "rouge"), (5, 6, "vert"), (2, 5, "jaune")]) == True

    # Cas gagnant : plus de 6 cartes, mais contient 6 identiques
    assert is_win([(1, 2, "bleu"), (3, 4, "bleu"), (5, 6, "bleu"), (2, 3, "bleu"), (4, 5, "bleu"), (6, 1, "bleu"), (2, 5, "rouge"), (3, 6, "vert")]) == True
    assert is_win([(1, 2, "jaune"), (3, 4, "rouge"), (5, 6, "vert"), (2, 3, "violet"), (4, 5, "orange"), (6, 1, "bleu"), (2, 5, "bleu"), (3, 6, "jaune")]) == True

    print("Tous les tests sont passés avec succès !")

#test_suites()