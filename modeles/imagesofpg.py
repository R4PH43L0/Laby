"""Images and pygame load."""
import pygame as pg
from constantes import *

"""Function for Perso Class"""
"""Imges loading in pygame."""

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

