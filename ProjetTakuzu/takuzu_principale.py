from takuzu_1NSI_eleve import *
from takuzu_algo import *

taille = 6
pourcentage = 20 # Le Pourcentage n'est pas exate il représante une donnée aléatoire

nom_fichier_grille = generer_grille_takuzu(taille, pourcentage)
#nom_fichier_grille = generer_grille_unique_takuzu(taille) # Pour générer une grille unique 

grille = lecture(nom_fichier_grille)

#Calcule le nombre de case vide dans la grille
nb_de_9 = 0
for ligne in grille:
    if 9 in ligne:
        nb_de_9 += ligne.count(9)
        
print("Grille vidée à hauteur de " + str(round(nb_de_9/(taille**2)*100, 2)) + "%")
affiche(grille)

solutions = resoudre_takuzu(grille)

print("\nVoici la (ou les) solution(s) trouvée(s) :  (", len(solutions) ,"solution(s) )")
for solution in solutions:
    affiche(solution)
    if(verif_nb_0_nb_1(solution) and verif_000_111(solution) and verif_ligne_colonne(solution)):
        print("Bravo, Grille valide")
    else:
        print("Erreur, Grille non valide")

#Possiblité d'utilisé une interface graphique
takuzu_graphique(lecture(nom_fichier_grille))


