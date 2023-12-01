import pygame
from constants import *
from assistant import Auxiliar





class Platform:
    
    def __init__(self, x, y, w, h, is_static=False, has_image=True, limit_top=None, limit_bottom=None):
        self.has_image = has_image
        self.is_static = is_static
        self.image = None if not has_image else Auxiliar.getSurfaceFromSpriteSheet("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/stage/ascensor.png", 1, 1)[0]
        self.image = pygame.transform.scale(self.image, (w, h)) if has_image else None
        self.rect = self.image.get_rect() if has_image else pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.y_inicial = y 

        

        # Se generan los rectángulos de colisión para la plataforma
        
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y + h - GROUND_RECT_H, self.rect.w, GROUND_RECT_H)
        self.rect_top_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

        self.direction = 1 if limit_top is not None and limit_bottom is not None else 0
        self.limit_top = limit_top
        self.limit_bottom = limit_bottom
        
    
    
        

    def draw(self, screen):
        
        if self.has_image:
            screen.blit(self.image, self.rect)
        if DEBUG:
            #pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            pygame.draw.rect(screen, BLUE, self.rect_top_collition)


    def update(self):
        print(f"{self.direction}")
        y_inicial = self.rect.y
        if self.is_static:
            self.direction = 0
            # Si es estática, no se actualiza la posición

        if self.direction != 0:
            self.rect.y += self.direction
            if self.has_image:
                self.rect_ground_collition.y += self.direction
                self.rect_top_collition.y += self.direction
            if self.rect.y <= self.limit_top or self.rect.y >= self.limit_bottom:
                self.direction *= -1
                
            elif self.rect.y >= self.limit_bottom:
                self.direction = -1
        else:
            self.rect.y = y_inicial


            
            
    def is_colliding(self, rect):
        return self.rect.colliderect(rect)
    


