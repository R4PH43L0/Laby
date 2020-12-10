import sys
import pygame
from tableaux import niveau


class perso(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


        self.image = pygame.image.load("assets/crapeaux.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (30, 30))

    def prt(self):
        ecran.blit(self.image, (self.x, self.y))

    def get_size(self):
        return self.image.get_size()

    def get_pos(self):
        return (self.x, self.y)


pygame.init()

ecran = pygame.display.set_mode((450, 450))

pygame.display.set_caption("Labyrinthe")

clock = pygame.time.Clock()

raph = perso()

# height = ecran.get_height()           # getting sizes to align center
# width = ecran.get_width()             #
# raph_h, raph_w = raph.get_size()      #

# raph.x = int(width / 2 - raph_w / 2)   # align center
# raph.y = int(height / 2 - raph_h / 2)  #

BLUE = (0, 120, 180)
# BLACK = (0, 0, 0)

# bleu = pygame.Surface((30, 30))
# bleu.fill(BLUE)

# noir = pygame.Surface((30, 30))
# noir.fill(BLACK)

                            # Imports des assets
                            # voir ci-dessous :
mur = pygame.image.load("assets/mur.jpg").convert_alpha()
mur = pygame.transform.scale(mur, (30, 30))

fond = pygame.image.load("assets/fond.png").convert_alpha()
fond = pygame.transform.scale(fond, (30, 30))


nenu = pygame.image.load("assets/nenuphar.png").convert_alpha()
nenu = pygame.transform.scale(nenu, (30, 30))

chat = pygame.image.load("assets/chat.png").convert_alpha()
chat = pygame.transform.scale(chat, (30, 30))

                            # Definitions des variables
nenuphar = 0
continuer = True

                            # Position de départ du Perso
raph.x = 30
raph.y = 30

def draw(ecran, niveau):                # parcour de la liste niveau puis,
                                        # blit des differents éléments
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                ecran.blit(mur, (i * 30, j * 30))
            elif case == 0:
                ecran.blit(fond,(i * 30, j * 30))
            elif case == 3:
                ecran.blit(nenu, (i * 30, j * 30))
            elif case == 2:
                ecran.blit(raph.image,(raph.x, raph.y))
                ecran.blit(fond, (i * 30, j * 30))
            elif case == 4:
                ecran.blit(chat, (i * 30, j * 30))

def mouv(x, y):                         # return False if wall
#    print(x, y)                        # else let the perso pass
    global nenuphar
    if niveau[y][x] == 1:
        return False
    elif niveau[y][x] == 0:
        return True
    elif niveau[y][x] == 2:
        return True
    elif niveau[y][x] == 3:
        return True
    elif niveau[y][x] == 4:
        if nenuphar == 5:
            print ("---  YOU WIN !!!  ---")
            print ("--- ",nenuphar,"Nenuphar catched !")
        else:
            print (" --- OOPS, YOU LOOSE. ---")
            print (" you have miss", 5 - nenuphar, "nenuphar")
        sys.exit()

def catch(x, y):                        # compte les nenuphars
    global nenuphar
    if niveau[y][x] == 3:
        niveau[y][x] = 0
        nenuphar += 1
        print ("NENUPHAR = ", nenuphar)


pressed_keys = {"right": False, "left": False, "up": False, "down": False}

while continuer:                        # boucle principale d'evenement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:       # touche enfoncé

            if event.key == pygame.K_RIGHT:                 #
                pressed_keys["right"] = True             #

            if event.key == pygame.K_LEFT:                  #
                pressed_keys["left"] = True             #

            if event.key == pygame.K_UP:                    #
                pressed_keys["up"] = True               #

            if event.key == pygame.K_DOWN:                  #
                pressed_keys["down"] = True              #

        elif event.type == pygame.KEYUP:             # touche relaché

            if event.key == pygame.K_LEFT:
                pressed_keys["left"] = False

            if event.key == pygame.K_RIGHT:
                pressed_keys["right"] = False

            if event.key == pygame.K_UP:
                pressed_keys["up"] = False

            if event.key == pygame.K_DOWN:
                pressed_keys["down"] = False

    x = int(raph.x // 30)
    y = int(raph.y // 30)
    catch(x, y)                         # Catch nenuphar

  # == True is implied here for the pressed_keys function
  #  and for the mouv function

    if pressed_keys["left"]:

        if raph.x > 0 and mouv(x - 1, y):
            raph.x -= 30
        else:
            raph.x = raph.x

    if pressed_keys["right"]:

        if  raph.x <= 390 and mouv(x + 1, y):
            raph.x += 30
        else:
            raph.x = raph.x

    if pressed_keys["up"]:
        if raph.y > 0 and mouv(x, y - 1):
            raph.y -= 30
        else:
            raph.y = raph.y

    if pressed_keys["down"]:
        if raph.y <= 390 and mouv(x, y + 1):
            raph.y += 30
        else:
            raph.y = raph.y

#                x, y = raph.get_pos()      # for debug only
#                print("X =", x, "Y =", y)  #

    ecran.fill(BLUE)                        # peint le fond
    clock.tick(14)
    draw(ecran, niveau)                     # dessine le niveau
    raph.prt()                              # dessine le perso
    pygame.display.update()                 # update de l'ecran à chaque boucle
                             # clock tik unused


pygame.quit()
