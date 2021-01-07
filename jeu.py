"""Labyrinthe."""
# -*- coding: utf-8 -*-


from os import getlogin
from tableaux import niveau
from modeles.perso import Perso
from constantes import *
from imagesofpg import *
import pygame as pg

NAME = getlogin()

pg.init()

pg.display.set_caption("Labyrinthe de %s " % NAME)

clock = pg.time.Clock()

raph = Perso()

# Position de départ du Perso
raph.x = 30
raph.y = 30


def draw(ecran, niveau):
    """Parcour de la liste niveau puis, blit des differents éléments."""
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                ecran.blit(mur, (i * 30, j * 30))
            elif case == 0:
                ecran.blit(fond, (i * 30, j * 30))
            elif case == 3:
                ecran.blit(nenu, (i * 30, j * 30))
            elif case == 2:
                ecran.blit(raph.image, (raph.x, raph.y))
                ecran.blit(fond, (i * 30, j * 30))
            elif case == 4:
                ecran.blit(chat, (i * 30, j * 30))


def mouv(x, y):
    """Return False if WALL else let the perso go on."""
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
            print("---  YOU WIN !!!  ---")
            print("--- ", NENUPHAR, "Nenuphars catched !")
        else:
            print(" --- OOPS, YOU LOOSE. ---")
            print(" you have miss", 5 - NENUPHAR, "nenuphar")
        quit()


def catch(x, y):
    """Compte les nenuphars."""
    global NENUPHAR
    if niveau[y][x] == 3:
        niveau[y][x] = 0
        NENUPHAR += 1
        print("NENUPHAR = ", NENUPHAR)


pressed_keys = {"right": False, "left": False, "up": False, "down": False}

# boucle principale d'evenement
while CONTINUER:
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

        if raph.x <= 390 and mouv(x + 1, y):
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

    ecran.fill(BLUE)             # peint le fond
    clock.tick(14)               # vitesse du perso quand la touche est enfoncé
    draw(ecran, niveau)          # dessine le niveau
    raph.imprime_perso()         # dessine le perso
    pg.display.update()          # update de l'ecran à chaque boucle


pg.quit()
