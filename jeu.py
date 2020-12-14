#/usr/bin/pgthon3
# -*- coding: utf-8 -*-

import sys
from os import getlogin
import pygame as pg
from tableaux import niveau


class Perso(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


        self.image = pg.image.load("assets/crapeaux.png").convert_alpha()

        self.image = pg.transform.scale(self.image, (30, 30))

    def imprime_Perso(self):
        ecran.blit(self.image, (self.x, self.y))

    def get_Size(self):
        return self.image.get_size()

    def get_Pos(self):
        return (self.x, self.y)

NAME = getlogin()

pg.init()

ecran = pg.display.set_mode((450, 450))

pg.display.set_caption("Labyrinthe de %s " %NAME)

clock = pg.time.Clock()

raph = Perso()

# height = ecran.get_height()           # getting sizes to align center
# width = ecran.get_width()             #
# raph_h, raph_w = raph.get_size()      #

# raph.x = int(width / 2 - raph_w / 2)   # align center for perso object
# raph.y = int(height / 2 - raph_h / 2)  #

BLUE = (0, 120, 180)
# BLACK = (0, 0, 0)

# bleu = pg.Surface((30, 30))
# bleu.fill(BLUE)

# noir = pg.Surface((30, 30))
# noir.fill(BLACK)

                            # Imports des assets
                            # voir ci-dessous :
mur = pg.image.load("assets/mur.jpg").convert_alpha()
mur = pg.transform.scale(mur, (30, 30))

fond = pg.image.load("assets/fond.png").convert_alpha()
fond = pg.transform.scale(fond, (30, 30))


nenu = pg.image.load("assets/nenuphar.png").convert_alpha()
nenu = pg.transform.scale(nenu, (30, 30))

chat = pg.image.load("assets/cat.png").convert_alpha()
chat = pg.transform.scale(chat, (30, 30))

                            # Definitions des variables
NENUPHAR = 0
CONTINUER = True

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
    global NENUPHAR
    if niveau[y][x] == 1:               # Wall
        return False
    elif niveau[y][x] == 0:             # Water
        return True
    elif niveau[y][x] == 2:             # The Frog
        return True
    elif niveau[y][x] == 3:             # Nenuphar
        return True
    elif niveau[y][x] == 4:             # THE BOSS
        if NENUPHAR == 5:
            print ("---  YOU WIN !!!  ---")
            print ("--- ",NENUPHAR,"Nenuphars catched !")

        else:
            print (" --- OOPS, YOU LOOSE. ---")
            print (" you have miss", 5 - NENUPHAR, "nenuphar")

        quit()
#        sys.exit(0)



def catch(x, y):                        # compte les nenuphars
    global NENUPHAR
    if niveau[y][x] == 3:
        niveau[y][x] = 0
        NENUPHAR += 1
        print ("NENUPHAR = ", NENUPHAR)


pressed_keys = {"right": False, "left": False, "up": False, "down": False}

while CONTINUER:                        # boucle principale d'evenement
    for event in pg.event.get():
        if event.type == pg.QUIT:
            CONTINUER = False
            
        elif event.type == pg.KEYDOWN:       # touche enfoncé

            if event.key == pg.K_RIGHT:                 #
                pressed_keys["right"] = True             #

            if event.key == pg.K_LEFT:                  #
                pressed_keys["left"] = True             #

            if event.key == pg.K_UP:                    #
                pressed_keys["up"] = True               #

            if event.key == pg.K_DOWN:                  #
                pressed_keys["down"] = True              #

        elif event.type == pg.KEYUP:             # touche relaché

            if event.key == pg.K_RIGHT:
                pressed_keys["right"] = False

            if event.key == pg.K_LEFT:
                pressed_keys["left"] = False

            if event.key == pg.K_UP:
                pressed_keys["up"] = False

            if event.key == pg.K_DOWN:
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
    clock.tick(14)                          # vitesse du perso quand touche enfoncé
    draw(ecran, niveau)                     # dessine le niveau
    raph.imprime_Perso()                     # dessine le perso
    pg.display.update()                 # update de l'ecran à chaque boucle


pg.quit()
