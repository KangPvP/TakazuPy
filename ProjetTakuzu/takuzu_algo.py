from random import *

def generer_grille_takuzu(grille):
    # Initialiser une grille avec des valeurs de 9
    remplir_grille(grille, 0, 0)
    return grille

def remplir_grille(grille, ligne, colonne):
    # Vérifier si on a atteint la fin de la grille
    if ligne == len(grille):
        return True
    
    # Calculer la prochaine ligne et colonne
    prochaine_ligne = ligne if colonne < len(grille) - 1 else ligne + 1
    prochaine_colonne = colonne + 1 if colonne < len(grille) - 1 else 0
    
    # Remplir la case actuelle avec 0 ou 1 et vérifier si la grille est valide
    for num in sample([0, 1], 2):
        grille[ligne][colonne] = num
        if est_valide(grille, ligne, colonne) and remplir_grille(grille, prochaine_ligne, prochaine_colonne):
            return True
        grille[ligne][colonne] = 9  # Remplacer par 9 si la grille n'est pas valide
    
    return False

def est_valide(grille, ligne, colonne):
    taille = len(grille)
    
    # Vérifie si une ligne ou une colonne contient plus de deux chiffres identiques consécutifs
    nb_zeros_ligne = 0
    nb_uns_ligne = 0
    nb_zeros_colonne = 0
    nb_uns_colonne = 0
    
    # Compter le nombre de 0 et de 1 dans la ligne et la colonne
    for i in range(taille):
        if grille[ligne][i] == '0':
            nb_zeros_ligne += 1
        elif grille[ligne][i] == '1':
            nb_uns_ligne += 1
        if grille[i][colonne] == '0':
            nb_zeros_colonne += 1
        elif grille[i][colonne] == '1':
            nb_uns_colonne += 1
    
    # Vérifier si le nombre de 0 ou de 1 dépasse la moitié de la taille de la grille
    if nb_zeros_ligne > taille // 2 or nb_uns_ligne > taille // 2 or nb_zeros_colonne > taille // 2 or nb_uns_colonne > taille // 2:
        return False
    
    # Vérifier s'il y a plus de deux chiffres identiques consécutifs dans une ligne ou une colonne
    if colonne >= 2:
        if grille[ligne][colonne - 2] == grille[ligne][colonne - 1] == grille[ligne][colonne]:
            return False
    if ligne >= 2:
        if grille[ligne - 2][colonne] == grille[ligne - 1][colonne] == grille[ligne][colonne]:
            return False
    
    return True

def resoudre_takuzu(grille):
    solutions = []
    resoudre_recursive(grille, solutions)
    return solutions

def resoudre_recursive(grille, solutions):
    taille = len(grille)

    if est_complete(grille):
        solutions.append([[grille[row][col] for col in range(len(grille[row]))] for row in range(len(grille))])
        return
    
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == 9:  # Si la case est vide (représentée par 9)
                for num in [0, 1]:
                    grille[i][j] = num
                    if est_valide(grille, i, j):
                        resoudre_recursive(grille, solutions)
                    grille[i][j] = 9  # Retour à une case vide (représentée par 9)

def est_complete(grille):
    for ligne in grille:
        if 9 in ligne:  # Vérifie s'il y a encore des cases vides (représentées par 9)
            return False
    return True

def affichier_grille(grille):
    for ligne in grille:
        print(' '.join(str(case) for case in ligne))

taille = 6
grille = [[9 for i in range(taille)] for i in range(taille)]
grille = generer_grille_takuzu(grille)  # Générer une grille de Takuzu de taille donnée

pourcentage_remplissage = 40  # Pourcentage de remplissage de la grille

# Remplir aléatoirement la grille partiellement avec des cases vides
for i in range(taille):
    for j in range(taille):
        if random() < (pourcentage_remplissage / 100):
            grille[i][j] = 9

print("Grille de Takuzu partiellement remplie :")
affichier_grille(grille)

solutions = resoudre_takuzu(grille)

print("\nToutes les solutions trouvées :")
for solution in solutions:
    affichier_grille(solution)
    print()