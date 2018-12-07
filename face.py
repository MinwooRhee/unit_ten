import pygame
import random


class Face:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.RED = (255, 48, 48)
        self.BLUE = (66, 134, 244)
        self.GREEN = (48, 255, 182)
        self.YELLOW = (255, 243, 112)
        self.PURPLE = (190, 112, 255)

    def draw_face(self, position):
        color_list = [self.RED, self.BLUE, self.GREEN, self.YELLOW, self.PURPLE]
        color_face = random.choice(color_list)
        pygame.draw.circle(self.main_surface, color_face, position, 70, 0)
        color_list.remove(color_face)
        pygame.draw.circle(self.main_surface, random.choice(color_list), (position[0] - 35, position[1] - 25), 15, 0)
        pygame.draw.circle(self.main_surface, random.choice(color_list), (position[0] + 35, position[1] - 25), 15, 0)
        pygame.draw.polygon(self.main_surface, random.choice(color_list),
                    [(position[0], position[1]), (position[0], position[1] - 15), (position[0] + 25, position[1])], 0)
        pygame.draw.rect(self.main_surface, random.choice(color_list), (position[0] - 35, position[1] + 25, 70, 30), 0)

        pygame.display.update()
