"""Class Perso, the item constructor."""

class Perso(object):
    """Definition of the item."""

    def __init__(self, x=0, y=0):
        """Definition of the position of the item with x and y."""
        self.x = x
        self.y = y

        self.image = pg.image.load("assets/crapeaux.png").convert_alpha()

        self.image = pg.transform.scale(self.image, (30, 30))

    def imprime_perso(self):
        """Blit function of pygame to print the item."""
        ecran.blit(self.image, (self.x, self.y))

    def get_size(self):
        """Return the size of the item."""
        return self.image.get_size()

    def get_pos(self):
        """Return the position of the item."""
        return (self.x, self.y)
