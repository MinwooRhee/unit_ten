# Minwoo Rhee
# 20181211
# assignment_ten.py
# click to draw faces

import pygame, sys
from pygame.locals import *
import face


pygame.init()
mainSurface = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption("Pygame faces")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            face1 = face.Face(mainSurface)
            face1 = face1.draw_face(pygame.mouse.get_pos())
