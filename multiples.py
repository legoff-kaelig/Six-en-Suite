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

    assert type(tirage) is list

    verif = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), ("bleu", "rouge", "vert", "jaune", "violet", "orange")] # Matrice de tuples recensant les nombres et couleurs pris en compte
    indiceTirage = 0 # Entier permettant de se localiser sur la valeur de la carte prise en compte
    indiceMultiples = 0 # Entier permettant de notter chaque occurence d'une même valeur de manière temporaire
    cartesMajority = [[],[]] # Matrice permettant de noter la valeur majoritaire de manière temporaire
    currentMajority = [[0, 0]] # Matrice permettant de noter la valeur majoritaire de manière temporaire mais un peu plus longtemps quand même
    cartesPiochables = [] # Liste des cartes piochables, la valeur retournée à la fin

    #( Boucle principale qui va parcourir <verif> et prendre ces valeurs en indice <i>

    for i in verif :

        #( Boucle secondaire qui va parcourir <i> et prendre ces valeurs en indice <j>

        for j in i :

            #( Boucle tertiaire qui va parcourir <tirage> et prendre ces valeurs en indice <k>

            for k in tirage :

                #( Condition qui va vérifier si la valeur de <k> en fonction de la nature de <j> est égale à l'élément <j> qui correspond à l'élément de vérification actuelle

                if j == k[indiceTirage] :

                    indiceMultiples += 1 # Ajoute 1 à l'entier <indiceMultiples> pour permettre de savoir combien d'occurences de <j> il y a dans <tirage>
                    
                    cartesMajority[0].append(k) # Ajoute la carte 

                    if k not in cartesPiochables :

                        cartesMajority[1].append(k)

                #)
                            
            #)

            if currentMajority[0][0] < indiceMultiples :

                currentMajority = [[indiceMultiples, j]]
                cartesPiochables = cartesMajority[0]
            
            elif currentMajority[0][0] == indiceMultiples and cartesMajority[1] != [] :

                currentMajority.append([indiceMultiples, j])
                cartesPiochables.append(cartesMajority[1])

            cartesMajority = [[],[]]
            indiceMultiples = 0
        
        #)

        indiceTirage = 2
    
    #)

    return cartesPiochables

print(multiples([(4, 5, 'orange'), (4, 4, 'orange'), (3, 4, 'orange'), (3, 7, 'orange'), (4, 4, 'vert'), (4, 4, 'bleu')]))
print(multiples([(4, 5, 'orange')]))