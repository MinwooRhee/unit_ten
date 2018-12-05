import pygame, sys
from pygame.locals import *
import face

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Pygame faces")

face1 = face.Face(mainSurface)
face1.draw_face()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
