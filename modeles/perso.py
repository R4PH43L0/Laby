"""Class Perso, the item constructor."""
import pygame as pg

from modeles.imprime import Drawing, item, youwin, youlose
from modeles.tableaux import niveau

imp = Drawing(pg.display.set_mode((450, 450)), niveau)


class Perso(object):
    """Definition of the item."""

    global nenuphar
    nenuphar = 0

    def __init__(self, x, y, niveau):
        """Definition of the position of the item with x and y."""
        self.x = x
        self.y = y
        assert isinstance(niveau, list)
        self.niveau = niveau
        self.image = item

    def imprime_perso(self):
        """Blit function of pygame to print the item."""
        imp.ecran.blit(self.image, (self.x, self.y))

    def get_size(self):
        """Return the size of the item."""
        return self.image.get_size()

    def get_pos(self):
        """Return the position of the item."""

        return (self.x, self.y)

    def the_boss(self):
        """What to do when you meet the Boss."""

        if nenuphar == 5:
            print("---  YOU WIN !!!  ---")
            print("--- ", nenuphar, "Nenuphars catched !")
            imp.ecran.blit(youwin, (0, 0))
            pg.display.update()
            pg.time.delay(4000)
        else:
            print(" --- OOPS, YOU LOOSE. ---")
            print(" you have miss", 5 - nenuphar, "nenuphar")
            imp.ecran.blit(youlose, (0, 0))
            pg.display.update()
            pg.time.delay(4000)
        quit()

    def mouv(self, x, y):
        """Return False if WALL else let the perso go on."""

        if self.niveau[y][x] == 1:  # Wall
            return False
        elif self.niveau[y][x] == 0:  # Water
            return True
        elif self.niveau[y][x] == 2:  # The Frog
            return True
        elif self.niveau[y][x] == 3:  # Nenuphar
            return True
        elif self.niveau[y][x] == 4:  # THE BOSS
            self.the_boss()

    def catch(self, x, y):
        """Compte les nenuphars."""

        global nenuphar
        if self.niveau[y][x] == 3:
            self.niveau[y][x] = 0
            nenuphar += 1
            print("NENUPHAR = ", nenuphar)

    def mouvement(self, direction):
        """Movements of the Item."""

        x = int(self.x // 30)
        y = int(self.y // 30)

        self.catch(x, y)

        if direction == "left":
            if self.x > 0 and self.mouv(x - 1, y):
                self.x -= 30
            else:
                self.x = self.x
        if direction == "right":
            if self.x <= 390 and self.mouv(x + 1, y):
                self.x += 30
            else:
                self.x = self.x
        if direction == "up":
            if self.y > 0 and self.mouv(x, y - 1):
                self.y -= 30
            else:
                self.y = self.y
        if direction == "down":
            if self.y <= 390 and self.mouv(x, y + 1):
                self.y += 30
            else:
                self.y = self.y
