import pygame
from constants import *
from assistant import Auxiliar

class level_stage:
    def __init__(self):
        self.rect = [
            pygame.Rect(0, 510, 230, GROUND_RECT_H),
            pygame.Rect(360, 510, 30, GROUND_RECT_H),
            pygame.Rect(522, 510, 31, GROUND_RECT_H),
            pygame.Rect(683, 510, 33, GROUND_RECT_H),
            pygame.Rect(845, 510, 34, GROUND_RECT_H),
            pygame.Rect(1010, 510, 300, GROUND_RECT_H)
        ]

    def draw(self, screen):
        if DEBUG:
            for rect in self.rect:
                pygame.draw.rect(screen, BLUE, rect)

