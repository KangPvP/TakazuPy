import pygame

def affiche_graphique(a, x0, y0, cote, f):
    
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
            pygame.draw.rect(f, couleur_black, case,2)

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

                f.blit(texte,texte_rect)

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

    fonte = pygame.font.SysFont(None, 90)
    texte = fonte.render("Valider", True,(0,0,0))
    texte_rect = texte.get_rect()
    texte_rect.center = rectangle.center
    ecran.blit(texte,texte_rect)

    return rectangle

# Initialiser Pygame
pygame.init()

# Créer la fenêtre de jeu
xm, ym = 500, 500
a = [[1 for i in range(10)] for y in range(10)]
hauteur = len(a)
largeur = len(a[0])

x0, y0, case = cal_data_grille(largeur, hauteur)

ZoneCustom = pygame.Rect(x0, y0, largeur * case, hauteur * case)


ecran = pygame.display.set_mode([900,700])
pygame.display.set_caption("Takuzu")
ecran.fill((255,255,255))
affiche_titre(ecran)
affiche_btn(ecran)
affiche_graphique(a, x0, y0, case, ecran)
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

                if not a[nbY][nbX] == 0 and not a[nbY][nbX] == 1:
                    if a[nbY][nbX] == 2:
                        a[nbY][nbX] = 3
                    else:
                        a[nbY][nbX] = 2

                affiche_graphique(a, x0, y0, case, ecran)
                pygame.display.flip()

# Quitter Pygame
pygame.quit()