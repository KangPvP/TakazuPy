from random import *


def rotation(g) :
    """ Cette fonction construit la transposée d'une grille carrée (les lignes de la grille de départ deviennent les colonnes et inversement en gardant l'ordre).
    Paramètre : (list) une liste de liste g de taille carrée
    Sortie : (list) une liste de liste de taille carrée correspondant à la transposée de g
    """

    n = len(g)
    grilleRotate = [[0] * n for i in range(n)]

    for i in range(n):

        for j in range(n):
            grilleRotate[j][i] = g[i][j]

    return grilleRotate


def verif_nb_0_nb_1(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, le nombre de 0 et de 1 est égal à niveau/2.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 par ligne et par colonne (Règle 1) 
    """ 
    
    #Test les lignes et les colonnes
    if( verif_0_1_boucle(g) and verif_0_1_boucle(rotation(g)) ):
        return True
    else:
        return False

    

def verif_0_1_boucle(g):
    """Fonction en lien avec verif_nb_0_nb_1(g)""" 
    for l in range(len(g)):
        nb0, nb1 = 0, 0
        for c in range(len(g[0])):
            if(g[l][c] == 0 or g[l][c] == 2):
                nb0 = nb0 + 1
            elif(g[l][c] == 1 or g[l][c] == 3):
                nb1 = nb1 + 1
        if(nb0 != nb1):
            return False
        
    return True

def verif_000_111(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, il n'y a jamais plus de deux 0 ou de deux 1 adjacents
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 adjacent par ligne et par colonne (Règle 2)
    """

    if( verif_000_111_boucle(g) and verif_000_111_boucle(rotation(g)) ):
        return True
    else:
        return False

def verif_000_111_boucle(g) :
    """Fonction en lien avec verif_000_111_boucle(g)""" 
    for l in range(len(g)):
        nbAdj0, nbAdj1 = 0, 0
        for c in range(len(g[0])):
            if(g[l][c] == 0 or g[l][c] == 2):
                nbAdj1 = 0 #Reset nbAdj1 si 0
                nbAdj0 = nbAdj0 + 1

            elif(g[l][c] == 1 or g[l][c] == 3):
                nbAdj0 = 0 #Reset nbAdj0 si 1
                nbAdj1 = nbAdj1 + 1

            if(nbAdj0 > 2 or nbAdj1 > 2):
                return False
    return True
    

def verif_ligne_colonne(g) :
    """ Cette fontion vérifie que chaque ligne et chaque colonne de la grille g entrée en paramètre est unique.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau des lignes et des colonnes, chacune est unique (Règle 3)
    """ 

    if( verif_ligne_colonne_boucle(g) and verif_ligne_colonne_boucle(rotation(g)) ):
        return True
    else:
        return False
    
def verif_ligne_colonne_boucle(g):
    """Fonction en lien avec verif_ligne_colonne(g)""" 

    ltest = []
    for l in g:
        if l not in ltest:
            ltest.append(l)
        else:
            return False
        
    return True

print("oik")
