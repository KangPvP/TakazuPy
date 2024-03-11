from takuzu_1NSI_eleve import *
from takuzu_algo import *

taille = 12
pourcentage = 0
nberr = 0
for i in range(10):
    nom_fichier_grille = generer_grille_takuzu(taille, pourcentage)
    #nom_fichier_grille = generer_grille_unique_takuzu(taille) # Pour générer une grille unique 

    grille = lecture(nom_fichier_grille)

    #Calcule le nombre de case vide dans la grille
    nb_de_9 = 0
    for ligne in grille:
        if 9 in ligne:
            nb_de_9 += ligne.count(9)

    solutions = resoudre_takuzu(grille)
    #print("\nVoici la (ou les) solution(s) trouvée(s) :  (", len(solutions) ,"solution(s) )")
    # for solution in solutions:
    #     affiche(solution)
    #     print("")
    
    if(verif_nb_0_nb_1(grille) and verif_000_111(grille) and verif_ligne_colonne(grille)):
        print("Bravo, Grille valide")
    else:
        nberr+=1
        print("erreur")

print(nberr)






#Possiblité d'utilisé une interface graphique

#takuzu_graphique(lecture(nom_fichier_grille))


