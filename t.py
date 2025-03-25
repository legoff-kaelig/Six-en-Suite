bulletins=["Martin","Paul","Pierre","Jacques","Toto","Marie","Paul","Pierre","Jacques","Toto","Toto"]

def incr_dico(dico,cle):
    """ Entrée : un dictionnaire dico
                    une clef cle
        Sortie : rien (c'est une procédure qui modifie le dico existant)
        Effet : 
            - si cle est une clef de dico, la valeur de cle est augmentée de 1
            - sinon cle est insérée dans dico associée à la valeur 1
    """
    #
    # à compléter
    #
    if cle in dico:
        dico[str(cle)] += 1
    else: 
        dico[str(cle)] = 1
    
def depouillement(bulletins):
    """ Entrée : une liste bulletins
        Sortie : une chaîne de caractères : vainqueur
        Effets : 
           - construit le dictionnaire des noms-nb de bulletins
           - détermine le vainqueur
    """
    dico = {}
    ## création du dictionnaire
    #
    # à compléter
    #
    for vote in bulletins:
        incr_dico(dico,vote)
    ## détermination du vainqueur
    #
    # à compléter
    #
    vainqueur=""
    
    vainqueur = max(dico, key=dico.get)
    
    return vainqueur

print("le vainqueur est :",depouillement(bulletins))