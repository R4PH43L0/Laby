"""Labyrinthe."""
# -*- coding: utf-8 -*-


from os import getlogin
from modeles.tableaux import niveau
from modeles.perso import Perso
from constantes import *
from imagesofpg import *
import pygame as pg

NAME = getlogin()

pg.init()

pg.display.set_caption("Labyrinthe de %s " % NAME)

clock = pg.time.Clock()

raph = Perso(30, 30, niveau)

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


# == True is implied here for the pressed_keys function
#  and for the mouv function

    if pressed_keys["left"]:
        raph.mouvement("left")

    if pressed_keys["right"]:
        raph.mouvement("right")

    if pressed_keys["up"]:
        raph.mouvement("up")

    if pressed_keys["down"]:
        raph.mouvement("down")



    ecran.fill(BLUE)             # peint le fond
    clock.tick(14)               # vitesse du perso quand la touche est enfoncé
    draw(ecran, niveau)          # dessine le niveau
    raph.imprime_perso()         # dessine le perso
    pg.display.update()          # update de l'ecran à chaque boucle


pg.quit()
