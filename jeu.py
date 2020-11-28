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
pygame.display.set_caption("Laby")
clock = pygame.time.Clock()
raph = perso()
height = ecran.get_height()
width = ecran.get_width()
raph_h, raph_w = raph.get_size()
"""raph.x = int(width / 2 - raph_w / 2)
raph.y = int(height / 2 - raph_h / 2)"""
BLUE = (0, 100, 200)
BLACK = (0, 0, 0)
mur = pygame.Surface((30, 30))
mur.fill(BLACK)
"""raph.prt()
ecran.fill(GREY)"""
continuer = True
"""raph.x = int(30)
raph.y = int(30)"""


def draw(ecran, niveau):
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                ecran.blit(mur, (i * 30, j * 30))


def one(x, y):
    print(x, y)

    if niveau[y][x] == 1:
        return False
    elif niveau[y][x] == 0:
        return True
    elif niveau[y][x] == 2:
        pass


raph.x = 30
raph.y = 30

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            x = int(raph.x // 30)
            y = int(raph.y // 30)
            one(x, y)
            if event.key == pygame.K_RIGHT:
                print("right")
                if one(x + 1, y):
                    raph.x += 30
                else:
                    raph.x = raph.x
            if event.key == pygame.K_LEFT:
                print("left")
                if one(x - 1, y):
                    raph.x -= 30
                else:
                    raph.x = raph.x
            if event.key == pygame.K_UP:
                print("up")
                if one(x, y - 1):
                    raph.y -= 30
                else:
                    raph.y = raph.y
            if event.key == pygame.K_DOWN:
                print("down")
                if one(x, y + 1):
                    raph.y += 30
                else:
                    raph.y = raph.y
                """x, y = raph.get_pos()
                print("X =", x, "Y =", y)"""
            """if event.type == pygame.QUIT:
                continuer = False
                sys.exit()"""
    ecran.fill(BLUE)
    draw(ecran, niveau)
    raph.prt()
    pygame.display.update()
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
