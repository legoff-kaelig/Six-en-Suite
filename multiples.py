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

    for i in verif:

        print("i :",i)

        for j in i:

            print("j :",j)

            for k in tirage:

                print("k :",k)

                if j == k[indiceVerif]:

                    indiceMultiples += 1
                
                print("indicesMultiples :",indiceMultiples)
            
            if currentMajority[0][0] < indiceMultiples:

                currentMajority = [[indiceMultiples, j]]
            
            elif currentMajority[0][0] == indiceMultiples:

                currentMajority.append([indiceMultiples, j])

            indiceMultiples = 0

        indiceVerif = 2

        print(currentMajority)

multiples([(10, 0, "bleu") , (10, 3, "bleu") , (11, 3, "orange") , (11, 3, "violet")])
