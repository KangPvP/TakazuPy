from random import*
from copy import* 
import pygame, sys
## Utilisation fichier
## Mode d'emploi

# Pour jouer en mode console, on éxecute la commande takuzu('grille4x4_1') pour jouer avec la grille correspondante qui est donnée en format .txt.
# Pour jouer en mode graphique sur pygame, on éxecute la fonction takuzu_graphique('grille4x4_1') pour jouer avec la grille correspondante qui est donnée en format .txt.

#
###
#####
####################@
#####
###
#

## Création et affichage de la grille

# Fonction de lecture de la situation de départ
def lecture(nom_fic):
    """Cette fonction prend en paramètre :
    - une chaine de caractères désignant un nom de fichier (sans l'extension .txt)
    Elle renvoie une liste de liste grille contenant des 0, des 1 et des 9 représentant la situation de départ dans la grille de takuzu avec :
    grille[l][c] contient 0 si la case de la ligne l et de la colonne c contient 0, 1 si elle contient 1 et 9 si elle est vide
    """
    fichier = open(nom_fic + '.txt', 'r')
    tempo = []
    # Parcours des lignes du fichier :
    for ligne in fichier:
        tempo.append(list(ligne.strip()))
    # Fermeture du fichier :
    fichier.close()
    # Conversion des éléments en 0/1 à la place de '0'/'1'
    automate = [ [ int(tempo[l][c]) for c in range(len(tempo[l])) ] for l in range(len(tempo))]

    return automate


def affiche(g):
    """Cette fonction affiche la grille formatée comme il faut dans la console d'éxecution
    paramètre : (list) liste de liste carré et de taille pair
    """

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(g)):
        ligne = ""

        #Execution 1 seul fois pour la première ligne et pour affichier le numéro de chaque colonne
        if(i == 0):
            for y in range(len(g[0])):
                ligne = ligne + " " + str(y+1)
            print(" " + ligne)
            ligne = "" #Remise à 0 de la variable Ligne

        for y in range(len(g[0])):
            if(y == len(g[i])-1): #Execution a l'arrivé du derniere chiffre de chaque ligne pour ne pas afficher: |
                ligne = ligne + replaceCaractere(g[i][y])
            else:
                ligne = ligne + replaceCaractere(g[i][y]) + "|"

        print(alpha[i] + " " + ligne)

    return

def replaceCaractere(a):
    if(a == 9):
        return "*"
    elif(a == 0 or a == 2):
        return "0"
    elif(a == 1 or a == 3):
        return "1"


#
###
#####
####################@
#####
###
#
             


## Fonctions de jeu

    
def demande_coup() :
    """ Fonction qui demande au joueur la case dans laquelle il souhaite jouer et la valeur du coup jouée.
    Paramètre : aucun
    Sortie : (str,int) une chaine de caractère correspondant au coup joué et un entier correspondant à la valeur du coup joué.
    """ 
    case = input("Dans quel case souhaites tu joué ?")

    valeur = input("Veux tu mettre un 1 ou un 0 dans cette case ?")

    return (case, valeur)

    
def coord_coup_joue(case) :
    """ Fonction qui transforme la case jouée par le joueur au format texte (exemple A1) en coordonnées entières pour retrouver la valeur dans la grille de Takuzu au format liste de liste.
    Paramètre : (str) une chaine de caractère de longueur 2 au format attendu.
    Sortie : (int,int) un couple d'entiers correspondant à la case jouée dans la grille de Takuzu.
    """

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ligne = alpha.index(case[0])
    colonne = int(case[1])-1

    return (ligne, colonne)


#Modification de la fonction pour que la ligne et la collonne prenne un tuple en paramètre
def joue_coup(g,l,c,v) :
    """ Fonction qui joue un coup dans la grille g à la ligne l colonne c avec la valeur v.
    Paramètres : (liste,int,int,int) une grille g de Takuzu au format liste de liste, un entier l correspondant à la ligne jouée, un entier c correspondant à la colonne jouée, un entier v (0 ou 1) correspondant à la valeur jouée.
    Sortie : (list) la grille g de Takuzu au format liste de liste mise à jour avec la valeur jouée.
    """
    
    if(v == 0):
        g[l][c] = 2
    else:
        g[l][c] = 3

    return g


def grille_remplie(g):
    """ Fonction qui vérifie si la grille g de TAKUZU entrée en paramètre contient des cases non jouées.
    Paramètre : (list) une grille de Takuzu au format liste de liste
    Sortie : (bool) un booléen indiquant si la grille de Takuzu est complète
    """
    for l in range(len(g)):
        for c in range(len(g[0])):
            if (g[l][c] == 9):
                return False

    return True

def verification(grille, colonne, ligne, valeur):
    
    #Ligne qui test si la case demandé existe ex: A7
    if ligne < 0 or ligne >= len(grille) or colonne < 0 or colonne >= len(grille[0]):
        return (False, "Cette case n'est pas présante merci de renseigner une autre case")
    
    if grille[ligne][colonne] == 0 or grille[ligne][colonne] == 1:
        return (False, "Cette case ne peut pas être modifié")
    
    if valeur not in [0, 1]: 
        return (False, "Valeur saisi est incorrect: entrez 0 ou 1")

    return (True, "")

def takuzu(grille) :
    """ Fonction qui gère le déroulement d'une partie de TAKUZU """
    affiche(grille)

    while not grille_remplie(grille):
        case, valeur = demande_coup()
        ligne, colonne = coord_coup_joue(case)
        
        status, msgError = verification(grille, ligne, colonne, int(valeur))

        if status:
            grille = joue_coup(grille, ligne, colonne, int(valeur))
            affiche(grille)
        else:
            print(msgError)

    print("Bravo")

#takuzu(lecture("grille4x4_1"))



#####
####################@
#####
###
#     

## Fonctions pour tester la validité d'une grille avec les 3 règles
        


def rotation(g) :
    """ Cette fonction construit la transposée d'une grille carrée (les lignes de la grille de départ deviennent les colonnes et inversement en gardant l'ordre).
    Paramètre : (list) une liste de liste g de taille carrée
    Sortie : (list) une liste de liste de taille carrée correspondant à la transposée de g
    """
    pass


def verif_nb_0_nb_1(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, le nombre de 0 et de 1 est égal à niveau/2.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 par ligne et par colonne (Règle 1) 
    """ 
    pass          
 
    
def verif_000_111(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, il n'y a jamais plus de deux 0 ou de deux 1 adjacents
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 adjacent par ligne et par colonne (Règle 2)
    """ 
    pass
    

def verif_ligne_colonne(g) :
    """ Cette fontion vérifie que chaque ligne et chaque colonne de la grille g entrée en paramètre est unique.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau des lignes et des colonnes, chacune est unique (Règle 3)
    """ 
    pass

  
#
###
#####
####################@
#####
###
# 


## Version Graphique (BONUS)


# À FAIRE POUR CEUX QUI LE SOUHAITENT


def takuzu_graphique():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


    pygame.quit()

takuzu_graphique()
