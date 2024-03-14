from random import *
from takuzu_regle_verif import *


def generer_grille_takuzu(taille, pourcentage_remplissage):
    """Cette fonction permet de générer une grille de takuzu valide et d'enregister cette grille dans un ficher .txt
    Paramètres: 
    - taille (int) la taille de la grille
    - pourcentage_remplissage (int) pourcentage des valeurs à retirer dans la grille
    Sortie: (string) nom du fichier dans le quel la grille à été enregister"""

    assert taille%2 == 0 and taille>3 and taille<13, "la taille de la grille doit être un nombres pairs, compris entre 3 et 13"

    # Création d'une grille vide avec des 9
    grille = [[9 for i in range(taille)] for i in range(taille)]
    remplir_grille(grille, 0, 0)

    while(not verif_ligne_colonne(grille)):  # Teste si la grille générer est correct
        grille = [[9 for i in range(taille)] for i in range(taille)]
        remplir_grille(grille, 0, 0)

    # Cette boucle retire un certain % des valeurs dans la grille
    for i in range(taille):
        for j in range(taille):
            if random() < (pourcentage_remplissage / 100):
                grille[i][j] = 9

    nom_fichier = grilleToFichier(grille)

    return nom_fichier

def remplir_grille(grille, ligne, colonne):
    """Cette fonction est une fonction récurscive qui remplit la grille de takuzu
    Paramètres:
    - grille (list) une grille de takuzu
    - ligne (int) numéro de la ligne
    - colonne (int) numéro de la colonne
    Sortie: (boolean) indiquant si la grille est valide"""
    # Vérifier si on a atteint la fin de la grille
    if ligne == len(grille):
        return True
    
    # Calculer la prochaine ligne et colonne
    if colonne < len(grille) - 1:
        prochaine_ligne = ligne 
    else:
        prochaine_ligne = ligne + 1

    if colonne < len(grille) - 1:
        prochaine_colonne = colonne + 1 
    else:
        prochaine_colonne = 0
    # Remplir la case actuelle avec 0 ou 1 et vérifier si la grille est valide
    for num in sample([0, 1], 2):
        grille[ligne][colonne] = num
        if est_valide(grille, ligne, colonne) and remplir_grille(grille, prochaine_ligne, prochaine_colonne):
            return True
        grille[ligne][colonne] = 9  # Remplacer par 9 si la grille n'est pas valide
    
    
    return False

def est_valide(grille, ligne, colonne):
    """Cette fonction permet de savoir si à une emplacement donné dans la grille celle-ci est valide
    Paramètres:
    - grille (list) une grille de takuzu
    - ligne (int) numéro de la ligne
    - colonne (int) numéro de la colonne
    Sortie: (boolean) indiquant si la grille localement est valide"""

    taille = len(grille)
    
    # Vérifie si une ligne ou une colonne contient plus de deux chiffres identiques consécutifs
    nb_zeros_ligne = 0
    nb_uns_ligne = 0
    nb_zeros_colonne = 0
    nb_uns_colonne = 0
    
    # Compter le nombre de 0 et de 1 dans la ligne et la colonne
    for i in range(taille):
        if grille[ligne][i] == 0:
            nb_zeros_ligne += 1
        elif grille[ligne][i] == 1:
            nb_uns_ligne += 1
        if grille[i][colonne] == 0:
            nb_zeros_colonne += 1
        elif grille[i][colonne] == 1:
            nb_uns_colonne += 1
    
    # Vérifier si le nombre de 0 ou de 1 dépasse la moitié de la taille de la grille
    if nb_zeros_ligne > taille // 2 or nb_uns_ligne > taille // 2 or nb_zeros_colonne > taille // 2 or nb_uns_colonne > taille // 2:
        return False
    
    # Vérifier s'il y a plus de deux chiffres identiques consécutifs dans une ligne ou une colonne
    # Il y a 3 facon d'aligné 3 chiffres de facon consécutifs
    if colonne >= 2:
        if grille[ligne][colonne - 2] == grille[ligne][colonne - 1] == grille[ligne][colonne]:
            return False
    if colonne < taille - 2:
        if grille[ligne][colonne] == grille[ligne][colonne + 1] == grille[ligne][colonne + 2]:
            return False
    if colonne >= 1 and colonne < taille - 1:
        if grille[ligne][colonne - 1] == grille[ligne][colonne] == grille[ligne][colonne + 1]:
            return False

    if ligne >= 2:
        if grille[ligne - 2][colonne] == grille[ligne - 1][colonne] == grille[ligne][colonne]:
            return False
    if ligne < taille - 2:
        if grille[ligne][colonne] == grille[ligne + 1][colonne] == grille[ligne + 2][colonne]:
            return False
    if ligne >= 1 and ligne < taille - 1:
        if grille[ligne - 1][colonne] == grille[ligne][colonne] == grille[ligne + 1][colonne]:
            return False
    
    # Vérifier si deux lignes ou deux colonnes sont identiques
    for i in range(taille):
        ligne1 = grille[ligne]
        ligne2 = grille[i]

        if i != ligne and ligne1 == ligne2:  # Comparaison de lignes
            return False
        
        # colonne1 = [grille[l][colonne] for l in range(taille)]
        # colonne2 = [grille[l][i] for l in range(taille)]
        # if colonne1.count(9) <= 4 and colonne2.count(9) <= 4:
        #     print(colonne1)
        #     if i != colonne and colonne1 == colonne2:  # Comparaison de colonnes
        #         return False

    return True



def resoudre_takuzu(grille):
    solutions = []
    solveur(grille, solutions)

    return solutions

def solveur(grille, solutions):
    """Cette fonction est une fonction récurscive qui permet de resoudre une grille avec toutes les solutions possible
    Paramètres"""
    taille = len(grille)

    if est_complete(grille):
        if(verif_ligne_colonne(grille)):  # Teste si la solution est correct
            solutions.append([[colonne for colonne in ligne] for ligne in grille])
        return
    
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == 9:  # Si la case est vide (représentée par 9)
                for num in [0, 1]:
                    grille[i][j] = num
                    if est_valide(grille, i, j):
                        solveur(grille, solutions)
                    grille[i][j] = 9  # Retour à une case vide (représentée par 9)
                return
    return

def est_complete(grille):
    for ligne in grille:
        if 9 in ligne:  # Vérifie s'il y a encore des cases vides (représentées par 9)
            return False
    return True


def grilleToFichier(grille):
    """Cette fonction permet d'enregister la grille dans un fichier .txt
    Paramètre: (list) une grille de takuzu
    Sortie: (string) le nom du fichier .txt"""
    taille = len(grille)

    # Creation du nom du fichier    
    aleatoireNumber = randint(100,999)
    nom_fichier = "grille" + str(taille) + "x" + str(taille) + "_" + str(aleatoireNumber)

    # Ecriture à l'interieur du fichier
    fichier = open(nom_fichier+ ".txt", "w+", encoding='utf-8')
    
    for i in range(taille):
        for y in range(taille):
            fichier.write(str(grille[i][y]))
        fichier.write("\n")
        
    fichier.close()

    return nom_fichier

def generer_grille_unique_takuzu(taille):
    """Cette fonction permet de générer une grille de takuzu valide et d'enregister cette grille dans un ficher .txt
    Paramètres: 
    - taille (int) la taille de la grille
    - pourcentage_remplissage (int) pourcentage des valeurs à retirer dans la grille
    Sortie: (string) nom du fichier dans le quel la grille à été enregister"""

    assert taille%2 == 0 and taille>3 and taille<13, "la taille de la grille doit être un nombres pairs, compris entre 3 et 13"

    # Création d'une grille vide avec des 9
    grille = [[9 for i in range(taille)] for i in range(taille)]
    remplir_grille(grille, 0, 0)

    while(not verif_ligne_colonne(grille)):  # Teste si la grille générer est correct
        grille = [[9 for i in range(taille)] for i in range(taille)]
        remplir_grille(grille, 0, 0)

    # Cette boucle retire un certain % des valeurs dans la grille
    nb_solution = 1
    save_grille = [[colonne for colonne in ligne] for ligne in grille]

    while nb_solution == 1:
        #Choisir une case aléatoire dans la grille
        save_grille = [[colonne for colonne in ligne] for ligne in grille]
        l = randint(0,taille-1)
        c = randint(0,taille-1)

        grille[l][c] = 9

        nb_solution = len(resoudre_takuzu(grille))

    nom_fichier = grilleToFichier(save_grille)

    return nom_fichier


