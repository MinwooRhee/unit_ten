import pygame, sys
from pygame.locals import *
import logo

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Pygame test window")

logo1 = logo.Logo(mainSurface)
logo1.draw_rectangles()
logo1.draw_trellis()
logo1.draw_words()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
