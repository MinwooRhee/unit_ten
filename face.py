import pygame


class Face:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.GREEN = (0, 102, 71)
        self.GOLD = (255, 209, 63)
        self.WHITE = (255, 255, 255)

    def draw_face(self):
        pygame.draw.circle(self.main_surface, self.GREEN, (100, 100), 70, 0)
        pygame.draw.circle(self.main_surface, self.GOLD, (100 - 35, 100 - 25), 15, 0)
        pygame.draw.circle(self.main_surface, self.GOLD, (100 + 35, 100 - 25), 15, 0)
        pygame.draw.polygon(self.main_surface, self.WHITE, [(100, 100), (100, 100 - 15), (100 + 25,100)], 0)
        pygame.draw.rect(self.main_surface, self.GOLD, (100 - 35, 100 + 25, 70, 30), 0)

        pygame.display.update()
