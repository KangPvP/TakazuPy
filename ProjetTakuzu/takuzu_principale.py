from takuzu_1NSI_eleve import *
from takuzu_algo import *

taille = 6
pourcentage = 40
#nom_fichier_grille = generer_grille_takuzu(taille, pourcentage)
nom_fichier_grille = generer_grille_unique_takuzu(taille) # Pour générer une grille unique 

grille = lecture(nom_fichier_grille)

#Calcule le nombre de case vide dans la grille
nb_de_9 = 0
for ligne in grille:
    if 9 in ligne:
        nb_de_9 += ligne.count(9)

print("Grille vidé a hauteur de ",nb_de_9*100//(taille**2), "%")

affiche(grille)

solutions = resoudre_takuzu(grille)

print("\nVoici la (ou les) solution(s) trouvée(s) :  (", len(solutions) ,"solution(s) )")
for solution in solutions:
    affiche(solution)
    print("")



#Possiblité d'utilisé une interface graphique

takuzu_graphique(lecture(nom_fichier_grille))


