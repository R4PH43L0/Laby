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



while continuer:                        # boucle principale d'evenement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:      # touche enfoncé

            x = int(raph.x // 30)
            y = int(raph.y // 30)
            catch(x, y)                         # Catch nenuphar

            if event.key == pygame.K_RIGHT:                 # MOVE RIGHT
#                print("right")             # debug only
                if  raph.x <= 390 and mouv(x + 1, y):
                    raph.x += 30
                else:
                    raph.x = raph.x

            if event.key == pygame.K_LEFT:                  # MOVE LEFT
#                print("left")              # debug only
                if mouv(x - 1, y) and raph.x > 0:
                    raph.x -= 30
                else:
                    raph.x = raph.x

            if event.key == pygame.K_UP:                    # MOVE UP
#                print("up")                # debug only
                if mouv(x, y - 1) and raph.y > 0:
                    raph.y -= 30
                else:
                    raph.y = raph.y

            if event.key == pygame.K_DOWN:                  # MOVE DOWN
#                print("down")              # debug only
                if raph.y <= 390 and mouv(x, y + 1):
                    raph.y += 30

                else:
                    raph.y = raph.y

#                x, y = raph.get_pos()      # for debug only
#                print("X =", x, "Y =", y)  #

    ecran.fill(BLUE)                        # peint le fond
    draw(ecran, niveau)                     # dessine le niveau
    raph.prt()                              # dessine le perso
    pygame.display.update()                 # update de l'ecran à chaque boucle
    clock.tick(60)                          # clock tik unused


pygame.quit()
