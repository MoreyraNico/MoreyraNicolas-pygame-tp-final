import pygame
from constants import *
from assistant import Auxiliar

class Platform:
    
    def __init__(self, x, y, w, h, is_static=False, has_image=True, recorrido_limite=None,velocidad=None,tope=None):
        self.has_image = has_image
        self.is_static = is_static
        self.image = None if not has_image else Auxiliar.getSurfaceFromSpriteSheet("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/stage/ascensor.png", 1, 1)[0]
        self.image = pygame.transform.scale(self.image, (w, h)) if has_image else None
        self.rect = self.image.get_rect() if has_image else pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.y_inicial = y        

        # Se generan los rectángulos de colisión para la plataforma        
        self.rect_ground_collition = pygame.Rect(self.rect.x+10, self.rect.y + h - GROUND_RECT_H, self.rect.w-20, GROUND_RECT_H)
        self.rect_top_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.tope = tope

        
        self.recorrido = 0        
        self.direction = 1
        self.velocidad = velocidad
        self.recorrido_limite = recorrido_limite

    def draw(self, screen):
        
        if self.has_image:
            screen.blit(self.image, self.rect)
        if DEBUG:
            #pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            pygame.draw.rect(screen, BLUE, self.rect_top_collition)


    def update(self):       
        if self.is_static:
            self.direction = 0     
            # Si es estática, no se actualiza la posición
        if not self.is_static:
            
            if self.direction != 0:
                #self.rect.y += 0
                self.rect.y += self.direction * self.velocidad         
                self.rect_ground_collition.y += self.direction * self.velocidad 
                self.rect_top_collition.y += self.direction * self.velocidad 

                self.recorrido += (abs(self.direction) * self.velocidad ) + self.y_inicial
                print(f"RECORRIDO {self.direction}  {self.recorrido}")
                self.y_inicial=0
                if self.direction > 0:  # Descendiendo                                 
                    if  self.recorrido == self.recorrido_limite:
                        
                        self.direction *= -1
                        self.recorrido = 0  # Reiniciar contador
                        self.y_inicial = 0
                    
                elif self.direction < 0:  # Ascendiendo                    
                    if self.recorrido == (self.recorrido_limite):
                        #print(f"RECORRIDO {self.direction}  {self.recorrido_limite}")
                        self.direction *= -1
                        self.recorrido = 0  # Reiniciar contador

    
    


