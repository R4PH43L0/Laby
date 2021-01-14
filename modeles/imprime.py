"""Class imprime labyrinthe ."""

import pygame as pg
from modeles.tableaux import niveau
from constantes import *


class Drawing(object):
    """Draw the Labyrinthe."""

    def __init__(self, ecran, niveau):
        self.ecran = ecran
        self.niveau = niveau

    def draw(self):
        """Parcour de la liste niveau puis, blit des differents éléments."""
        for j, ligne in enumerate(niveau):
            for i, case in enumerate(ligne):
                if case == 1:
                    self.ecran.blit(mur, (i * 30, j * 30))
                elif case == 0:
                    self.ecran.blit(fond, (i * 30, j * 30))
                elif case == 3:
                    self.ecran.blit(nenu, (i * 30, j * 30))
                elif case == 2:
                    self.ecran.blit(fond, (i * 30, j * 30))
                elif case == 4:
                    self.ecran.blit(chat, (i * 30, j * 30))


Drawing(pg.display.set_mode((450, 450)), niveau)

"""Iamges loading in pygame."""

item = pg.image.load(Crapeaux).convert_alpha()
item = pg.transform.scale(item, (30, 30))

mur = pg.image.load(Wall).convert_alpha()
mur = pg.transform.scale(mur, (30, 30))

fond = pg.image.load(Fond).convert_alpha()
fond = pg.transform.scale(fond, (30, 30))


nenu = pg.image.load(Nenu).convert_alpha()
nenu = pg.transform.scale(nenu, (30, 30))

chat = pg.image.load(Cat).convert_alpha()
chat = pg.transform.scale(chat, (30, 30))

youlose = pg.image.load(Lose)
youlose = pg.transform.scale(youlose, (450, 450))
youwin = pg.image.load(Win)
youwin = pg.transform.scale(youwin, (450, 450))
