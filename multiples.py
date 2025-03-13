#############################################################
# Six en Suite                                              #
# Fichier : multiples.py                                    #
# Auteurs : Kaelig LE GOFF, Riwan ROUSSEAU, Jules THAMIN    #
# Date : 03/2025                                            #
#############################################################

def multiples(tirage):
    '''
    Entrée :
    
        <tirage> : La matrice de tuples correspondant au tirage tiré par le joueur, en format [(carte, dé, couleur) , (...) , (carte, dé, couleur)] en fonction du nombre de cartes tirées.
        
    Sortie :
    
        <cartesPiochables> : Les cartes piochables par le joueur, en format [(carte, dé, couleur) , (...) , (carte, dé, couleur)] en fonction du nombre de cartes piochables.
    
    '''

    verif = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), ("bleu", "rouge", "vert", "jaune", "violet", "orange")]
    indiceVerif = 0
    indiceMultiples = 0
    currentMajority = [[0, 0]]
    cartesMajority = [[],[]]
    cartesPiochables = []

    for i in verif :

        for j in i :

            for k in tirage :

                if j == k[indiceVerif] :

                    indiceMultiples += 1
                    
                    cartesMajority[0].append(k)

                    if k not in cartesPiochables :

                        cartesMajority[1].append(k)
            
            if currentMajority[0][0] < indiceMultiples :

                currentMajority = [[indiceMultiples, j]]
                cartesPiochables = cartesMajority[0]
            
            elif currentMajority[0][0] == indiceMultiples :

                currentMajority.append([indiceMultiples, j])
                cartesPiochables.append(cartesMajority[1])

            cartesMajority = [[],[]]
            indiceMultiples = 0

        indiceVerif = 2

    return cartesPiochables

print(multiples([(4, 5, 'orange'), (4, 4, 'orange'), (3, 4, 'orange'), (3, 7, 'orange'), (4, 4, 'vert'), (4, 4, 'bleu')]))
print(multiples([(4, 5, 'orange'), (4, 4, 'orange'), (3, 4, 'orange')]))