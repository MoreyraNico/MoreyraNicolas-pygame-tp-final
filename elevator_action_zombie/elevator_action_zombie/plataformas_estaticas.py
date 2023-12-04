import pygame
from constants import *
from assistant import Auxiliar

class Platform_estatic:
    
    def __init__(self,x,y,w,h,type=0):
        
        self.rect_ground_collition = pygame.Rect(x, y, w, h)
        

    def draw(self,screen):       
        if(DEBUG):
            pygame.draw.rect(screen,BLUE,self.rect_ground_collition)