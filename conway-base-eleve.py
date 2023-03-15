### DM : jeu de la vie de Conway

## 1NSI - Nom :

import pygame
from random import random

## Exemple d'utilisation :

# simul_txt('automate1')

# ou :

# simul_graphique('automate1')

##





# Fonction de lecture de la situation de départ
def lecture(nom_fic):
    """Cette fonction prend en paramètre :
    - une chaine de caractères désignant un nom de fichier (sans l'extension .txt)
    Elle renvoie une liste de liste automate contenant des 0 et des 1 avec :
    automate[l][c] contient 0 si la case de la ligne l et de la colonne c représente une cellule morte et 1 si elle c'est une cellule vivante.
    """
    # Ouverture du fichier en mode lecture ('r'ead)
    fichier = open(nom_fic + '.txt', 'r')
    tempo = []
    # Parcours des lignes du fichier :
    for ligne in fichier:
        # On ajoute à automate la ligne :
        # - débarassée des espaces superflus (strip())
        # - transformée en liste de caractères (list( ... ))
        tempo.append(list(ligne.strip()))
    # Fermeture du fichier :
    fichier.close()
    # Conversion des éléments en 0/1 à la place de '0'/'1'
    automate = [ [ int(tempo[l][c]) for c in range(len(tempo[l])) ] for l in range(len(tempo))]
    return automate



# Fonction d'affichage d'un état (en mode texte)
def affiche(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle produit un affichage où :
    - une cellule morte est représentée par un '.'
    - une cellule vivante est représentée par un 'X'
    Elle ne renvoie rien.
    """
    # Remplacer pass par votre code :
    pass



# Fonction qui calcule le nombre de voisins vivants de chaque cellule
def compte_voisins(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle renvoie une liste de listes voisins telle que :
    voisins[l][c] contient le nombre de cellules voisines vivantes autour de la cellule de la ligne l et de la colonne c.
    """
    # Remplacer pass par votre code :
    pass




# Fonction de calcul de l'étape suivante
def calcul_etape(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle modifie la liste de listes automate représentant l'automate à l'étape suivante selon la règle :
    - si, à l'étape n, une cellule morte est entourée d'exactement 3 cellules vivantes, elle devient vivante à l'étape n+1
    - si, à l'étape n, une cellule vivante est entourée de 2 ou 3 cellules vivantes, elle reste vivante à l'étape n+1 et elle meurt sinon.
    Cette fonction renvoie un booléen indiquant si l'automate a été modifié
    """
    # Remplacer pass par votre code :
    pass



# Fonction d'écriture de fichier
def ecriture(nom_fic, etape, automate):
    """
    Cette fonction écrit un fichier texte de 0 et de 1 correspondant à l'état de l'automate. Elle prend pour paramètres :
    - nom_fic : chaine désignant la base du nom de fichier
    - etape : int
    - automate : liste de listes représentant l'automate à écrire.
    """
    # Création du nom de fichier :
    num = str(etape)
    zeros = '_'
    for i in range(4-len(num)):
        zeros += '0'
    # Ouverture du fichier :
    fichier = open(nom_fic + zeros + num + '.txt', 'w')
    # Récupération des dimensions :
    largeur = len(automate[0])
    hauteur = len(automate)
    # Ecriture :
    for l in range(hauteur):
        for c in range(largeur):
            fichier.write(str(automate[l][c]))
        # Passage à la ligne :
        fichier.write('\n')
    fichier.close()


## SIMULATION - VERSION TXT + écriture dans fichiers

def simul_txt(nom_fic, max_fic=20):
    """Cette fonction simule le jeu de la vie avec :
    - nom_fic : chaine désignant le nom du fichier initial et la base des fichiers à écrire.
    - max_fic : le nombre max de fichiers à écrire (par défaut 20)
    """
    pass



## DEBOGAGE :
def affiche_nb_voisins(automate):
    """Cette fonction peut vous aider à trouver vos erreurs.
    Elle prend en paramètre un automate
    Elle affiche au format texte dans la console la grille en remplaçant les 0 et les 1 par le nombre de voisins vivants de la cellule correspondante.
    Par exemple si un automate est représenté par :
    0000
    0110
    0010
    Cette fonction doit afficher :
    1221
    1222
    1322
    """
    # Remplacer pass par votre code :
    pass


## VERSION pygame de l'affichage
# Les trois fonctions qui suivent ne doivent pas être modifiées.

def simul_graphique(nom_fic):
    etape = 0
    # Dimensions zone d'affichage
    xm, ym = 500, 500
    # Lecture des données de départ
    a = lecture(nom_fic)
    hauteur = len(a)
    largeur = len(a[0])
    # côté d'une case
    case = xm // max(hauteur, largeur)
    # Position du coin haut-gauche de la première cellule
    x0 = 50 + (xm - case * largeur) // 2
    y0 = 50 + (ym - case * hauteur) // 2
    # Init fenêtre
    pygame.init()
    fenetre = pygame.display.set_mode([800,600])
    pygame.display.set_caption('Jeu de la vie de Conway')
    # Pour le taux de rafraichissement
    framerate = 1
    horaire = pygame.time.Clock()
    horaire.tick(framerate)

    # Booléen indiquant si l'état est encore modifié à chaque étape :
    modifie = True

    affiche_graphique(a, x0, y0, case, fenetre)
    affiche_consignes(fenetre, framerate)
    pygame.display.flip()
    debut = False

    # Début de simulation
    while modifie:
        horaire = pygame.time.Clock()
        horaire.tick(framerate)
        fenetre.fill((255,255,255))

        if debut:
            modifie = calcul_etape(a)
            affiche_graphique(a, x0, y0, case, fenetre)
            affiche_consignes(fenetre, framerate)
            etape = etape + 1
        else:
            affiche_graphique(a, x0, y0, case, fenetre)
            affiche_consignes(fenetre, framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                modifie = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    debut = True
                if event.key == pygame.K_a:
                    framerate = min(framerate + 1, 25)
                if event.key == pygame.K_r:
                    framerate = max(1, framerate - 1)
        # Rafraichissement de la fenêtre
        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        texte = fonte.render('Étape ' + str(etape), True, (0,0,255), (255,255,255))
        textRect = texte.get_rect()
        textRect.center = (650,550)
        fenetre.blit(texte, textRect)
        pygame.display.flip()

    pygame.quit()



def affiche_graphique(a, x0, y0, cote, f):
    hauteur = len(a)
    largeur = len(a[0])
    for l in range(hauteur):
        for c in range(largeur):
            if a[l][c] == 1:
                pygame.draw.rect(f, (0,255,0), [x0 + c*cote, y0+l*cote,cote,cote])
            else:
                pygame.draw.rect(f, (255,0,0), [x0 + c*cote, y0+l*cote,cote,cote])


def affiche_consignes(f, fr):
    fonte = pygame.font.SysFont('Comic Sans MS', 15)
    texte = fonte.render('Appuyer sur Entrée', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (700,100)
    f.blit(texte, textRect)

    texte = fonte.render('pour débuter la simulation', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (700,130)
    f.blit(texte, textRect)

    texte = fonte.render('sur a pour accélérer', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (700,160)
    f.blit(texte, textRect)

    texte = fonte.render('sur r pour ralentir', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (700,190)
    f.blit(texte, textRect)

    texte = fonte.render('framerate = ' + str(fr), True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (700,300)
    f.blit(texte, textRect)

## Fin de la version pygame



## BONUS

def crea_map_alea(lignes, colonnes, nom_fic, proba = .5):
    """Cette fonction prend en paramètres :
    - deux entiers lignes et colonnes désignant le nombre de lignes et de colonnes de la map à générer
    - un nom de fichier (sans extension) sous la forme d'une chaine
    - une proba indiquant la probabilité de créer une cellule vivante
    Elle créer la map aléatoirement qu'elle stocke dans le fichier (avec l'exetnsion .txt)
    """
    # Ouverture d'un fichier texte en mode écriture ('w'rite)
    fichier = open(nom_fic + '.txt', 'w')
    # Pour écrire un '1' dans le fichier on écrit :
    # fichier.write('1')
    # Pour écrire un saut de ligne, on écrit :
    #fichier.write('\n')

    # Ecrire votre code ici :

    # On ferme le fichier :
    fichier.close()




