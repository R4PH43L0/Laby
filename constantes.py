"""Constantes et images"""

import pygame as pg

ecran = pg.display.set_mode((450, 450))

BLUE = (0, 120, 180)

# Imports des assets
# voir ci-dessous :

item = pg.image.load("assets/crapeaux.png").convert_alpha()
item = pg.transform.scale(item, (30, 30))

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

