from random import shuffle

couleurs = ["bleu", "rouge", "vert", "jaune", "violet", "orange"]
paquet = []
for i in range(1,13): # La valeur de la Carte
    for j in range(1,7): # La valeur du Dé
        paquet.append((i, j, couleurs[((i + j) - 2) % 6]))
shuffle(paquet) # Mélange du paquet

