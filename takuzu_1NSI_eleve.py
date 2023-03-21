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
    """Cette fonction renvoie le caractère graphique utilisé pour l'affichage de la grille
    paramètre : (int) un caractères (chiffre) de la grille
    sortie: (str) le caractères graphique associer au paramètre
    """
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

#takuzu(lecture("grille4x4_1"))s



#####
####################@#
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

def takuzu_graphique(grille):

    # Initialisation de Pygame
    pygame.init()

    # Donnée relative au jeu
    hauteur = len(grille)
    largeur = len(grille[0])
    x0, y0, case = cal_data_grille(largeur, hauteur)
    ZoneCustom = pygame.Rect(x0, y0, largeur * case, hauteur * case)

    #Création de la fenetre
    ecran = pygame.display.set_mode([900,700])
    pygame.display.set_caption("Takuzu")

    ecran.fill((255,255,255))
    affiche_titre(ecran)
    affiche_btn(ecran)
    affiche_graphique(grille, x0, y0, case, ecran)
    pygame.display.flip()

    continuer = True
    while continuer:
        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable "continuer" à False
            if event.type == pygame.QUIT:
                continuer = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ZoneCustom.collidepoint(x, y):
                    nbX = (x - x0) // case
                    nbY = (y - y0) // case

                    if not grille[nbY][nbX] == 0 and not grille[nbY][nbX] == 1:
                        if grille[nbY][nbX] == 2:
                            grille[nbY][nbX] = 3
                        else:
                            grille[nbY][nbX] = 2

                    affiche_graphique(grille, x0, y0, case, ecran)
                    pygame.display.flip()
            

    # Quitter Pygame
    pygame.quit()

def affiche_graphique(a, x0, y0, cote, ecran):
    
    fonte = pygame.font.SysFont(None, 50)
    # Définir les couleurs
    couleur_aqua = (66,224,212)
    couleur_black = (0, 0, 0)
    couleur_blue = (0, 0, 255)

    hauteur = len(a)
    largeur = len(a[0])

    pygame.draw.rect(ecran, couleur_aqua, [x0, y0, largeur * cote, hauteur * cote])

    for l in range(hauteur):
        for c in range(largeur):
            case = pygame.Rect(x0 + c*cote, y0+l*cote,cote,cote)
            pygame.draw.rect(ecran, couleur_black, case,2)

            value, color, display = 9, couleur_black, True

            if a[l][c] == 0:
                value = 0
                color = couleur_blue
            elif a[l][c] == 2:
                value = 0
                color = couleur_black
            elif a[l][c] == 1:
                value = 1
                color = couleur_blue
            elif a[l][c] == 3:
                value = 1
                color = couleur_black
            else:
                display = False
            
            if(display):
                texte = fonte.render(str(value), True,color)
                texte_rect = texte.get_rect()
                texte_rect.center = case.center

                ecran.blit(texte,texte_rect)

    pygame.draw.rect(ecran, (0,0,0), [x0, y0, largeur * cote, hauteur * cote],5)



def cal_data_grille(largeur, hauteur): #Calcule de données relative a un Automate
    xm, ym = 500, 500

    case = xm // max(hauteur, largeur)
    x0 = 200 + (xm - case * largeur) // 2
    y0 = 85 + (ym - case * hauteur) // 2

    return x0, y0, case

def affiche_titre(ecran):
    fonte = pygame.font.SysFont(None, 90)
    texte = fonte.render("Takuzu", True,(0,0,0))
    texte_rect = texte.get_rect()
    texte_rect.center = (450,30)
    ecran.blit(texte,texte_rect)


def affiche_btn(ecran):
    rectangle = pygame.Rect(0,0,150,55)
    rectangle.center = 450, 640

    pygame.draw.rect(ecran, (0, 200, 0), rectangle, 0, 6)  # fond BTN
    pygame.draw.rect(ecran, (50, 50, 50), rectangle, 2, 6)  # contour BTN

    fonte = pygame.font.SysFont(None, 50)
    texte = fonte.render("Valider", True,(0,0,0))
    texte_rect = texte.get_rect()
    texte_rect.center = rectangle.center
    ecran.blit(texte,texte_rect)

    return rectangle

takuzu_graphique(lecture("grille4x4_1"))
