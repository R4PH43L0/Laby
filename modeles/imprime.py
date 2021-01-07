"""Class imprime labyrinthe ."""


from modeles.tableaux import niveau
from modeles.imagesofpg import *

class Drawing(object):
    """Draw the Labyrinthe."""
    def __init__(self, ecran, niveau):
        self.ecran = pg.display.set_mode((450, 450))
        self.niveau = niveau
    def draw(self):
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