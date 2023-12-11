import pygame
from constants import *
from assistant import Auxiliar

class Platform:
    
    def __init__(self, x, y, w, h, is_static=None, has_image=True, recorrido_limite=None,velocidad=None,tope=None):
        self.has_image = has_image
        self.is_static = is_static
        self.image = None if not has_image else Auxiliar.getSurfaceFromSpriteSheet("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/stage/ascensor.png", 1, 1)[0]
        self.image = pygame.transform.scale(self.image, (w, h)) if has_image else None
        self.rect = self.image.get_rect() if has_image else pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.y_inicial = y        

        # Se generan los rectángulos de colisión para la plataforma        
        self.rect_ground_collition = pygame.Rect(self.rect.x+10, self.rect.y + h - GROUND_RECT_H, self.rect.w-25, GROUND_RECT_H)
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
        #print("Estoy aca")    
        if self.is_static:
            self.direction = 0     
            # Si es estática, no se actualiza la posición
        if not self.is_static:
            
            if self.direction != 0:
                #self.rect.y += 0
                self.rect.y += self.direction * self.velocidad         
                self.rect_ground_collition.y += self.direction * self.velocidad 
                self.rect_top_collition.y += self.direction * self.velocidad 

                self.recorrido += (abs(self.direction) * self.velocidad )
                #print(f"RECORRIDO {self.direction}  {self.recorrido_limite}")
                
                if self.direction > 0:  # Descendiendo                                 
                    if  self.recorrido == (self.recorrido_limite):
                        
                        self.direction *= -1
                        self.recorrido = 0  # Reiniciar contador
                        self.y_inicial = 0
                    
                elif self.direction < 0:  # Ascendiendo                    
                    if self.recorrido == (self.recorrido_limite):
                        #print(f"RECORRIDO {self.direction}  {self.recorrido_limite}")
                        self.direction *= -1
                        self.recorrido = 0  # Reiniciar contador
'''
def creacion_plataformas():
    lista_plataformas = []
    
    lista_plataformas.append(Platform(553,45,130,130,is_static=False,has_image=True,recorrido_limite=460,velocidad=2))#Ascensor Principal
    lista_plataformas.append(Platform(228,45,130,130,is_static=False,has_image=True,recorrido_limite=350,velocidad=2))#Ascensor 02
    lista_plataformas.append(Platform(390,45,130,130,is_static=False,has_image=True,recorrido_limite=350,velocidad=2))#Ascensor 03
    lista_plataformas.append(Platform(715,45,130,130,is_static=False,has_image=True,recorrido_limite=350,velocidad=2))#Ascensor 04
    lista_plataformas.append(Platform(878,45,130,130,is_static=False,has_image=True,recorrido_limite=350,velocidad=2))#Ascensor 05
    
    lista_plataformas.append(Platform(0, 640, 800, GROUND_RECT_H, is_static=True, has_image=False))

    lista_plataformas.append(Platform(0, 510, 228, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(360, 510, 30, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(522, 510, 31, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(683, 510, 33, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(845, 510, 34, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(1010, 510, 300, GROUND_RECT_H, is_static=True, has_image=False))

    lista_plataformas.append(Platform(0, 390, 228, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(360, 390, 30, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(522, 390, 31, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(683, 390, 33, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(845, 390, 34, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(1010, 390, 300, GROUND_RECT_H, is_static=True, has_image=False))

    lista_plataformas.append(Platform(0, 280, 228, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(360, 280, 30, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(522, 280, 31, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(683, 280, 33, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(845, 280, 34, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(1010, 280, 300, GROUND_RECT_H, is_static=True, has_image=False))

    lista_plataformas.append(Platform(0, 168, 228, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(360, 168, 30, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(522, 168, 31, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(683, 168, 33, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(845, 168, 34, GROUND_RECT_H, is_static=True, has_image=False))
    lista_plataformas.append(Platform(1010, 168, 300, GROUND_RECT_H, is_static=True, has_image=False))

    lista_plataformas.append(Platform(0, 50, 2000, GROUND_RECT_H, is_static=True, has_image=False, tope=True))
    #lista_plataformas.append(Platform(360, 50, 30, GROUND_RECT_H, is_static=True, has_image=False))
    #lista_plataformas.append(Platform(522, 50, 31, GROUND_RECT_H, is_static=True, has_image=False))
    #lista_plataformas.append(Platform(683, 50, 33, GROUND_RECT_H, is_static=True, has_image=False))
    #lista_plataformas.append(Platform(845, 50, 34, GROUND_RECT_H, is_static=True, has_image=False))
    #lista_plataformas.append(Platform(1010, 50, 300, GROUND_RECT_H, is_static=True, has_image=False))

    #lista_plataformas.append(Platform(0, -500, 228, GROUND_RECT_H, is_static=True, has_image=False))
    return lista_plataformas
'''
