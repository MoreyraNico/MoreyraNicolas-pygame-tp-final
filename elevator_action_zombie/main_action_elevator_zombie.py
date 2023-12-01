

import pygame
import sys
from constants import *
from player import Player
from plataforma import Platform
from level_stage import level_stage
from plataformas_estaticas import Platform_estatic
from enemy import Enemy_zombie_uno

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("stage/stage_map.png")


#porcion_fondo = imagen_fondo.subsurface((0, 1530, 320, 320))
#porcion_fondo = pygame.transform.scale(porcion_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(x=0,y=400,speed_walk=8,speed_run=8,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10)
player_zombie = Enemy_zombie_uno(x=0,y=400,speed_walk=8,speed_run=8,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10)

#level = level_stage()
lista_plataformas_estaticas = []




lista_plataformas = []
lista_plataformas.append(Platform(553,100,130,130,limit_top=0, limit_bottom=500))
lista_plataformas.append(Platform(228,100,130,130,limit_top=0, limit_bottom=390))
lista_plataformas.append(Platform(390,200,130,130,limit_top=0, limit_bottom=390))
lista_plataformas.append(Platform(715,150,130,130,limit_top=0, limit_bottom=390))
lista_plataformas.append(Platform(878,250,130,130,limit_top=0, limit_bottom=390))

#lista_plataformas.append(Platform(0, 640, 800, GROUND_RECT_H, is_static=True, has_image=False))

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

lista_plataformas.append(Platform(0, 50, 228, GROUND_RECT_H, is_static=True, has_image=False))
lista_plataformas.append(Platform(360, 50, 30, GROUND_RECT_H, is_static=True, has_image=False))
lista_plataformas.append(Platform(522, 50, 31, GROUND_RECT_H, is_static=True, has_image=False))
lista_plataformas.append(Platform(683, 50, 33, GROUND_RECT_H, is_static=True, has_image=False))
lista_plataformas.append(Platform(845, 50, 34, GROUND_RECT_H, is_static=True, has_image=False))
lista_plataformas.append(Platform(1010, 50, 300, GROUND_RECT_H, is_static=True, has_image=False))

lista_plataformas.append(Platform(0, -500, 228, GROUND_RECT_H, is_static=True, has_image=False))

camera = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)

    
    posicion_fondo_y = 2048 - (1530 - camera) 
    #print(f"POSICION DEL FONDO:{posicion_fondo_y}")

    
    porcion_fondo = imagen_fondo.subsurface((0, 1530-camera, 320, 320))
    porcion_fondo = pygame.transform.scale(porcion_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    screen.blit(porcion_fondo, (0, 0))
    '''
    for level_rect in level.rect:
        if player_1.rect_ground_collition.colliderect(level_rect):
        # Ajusta la posición del personaje a la altura del rectángulo del nivel
            player_1.rect.y = level_rect.top - player_1.rect_ground_collition.height
            player_1.rect_ground_collition.y = level_rect.top - player_1.rect_ground_collition.height
            player_1.move_y = 0
            
            # Detiene el movimiento vertical del personaje
    '''
    for plataforma in lista_plataformas:
        plataforma.update()        
        plataforma.draw(screen)

    #for plataforma_estatica in lista_plataformas_estaticas:              
        #plataforma_estatica.draw(screen)

    #level.draw(screen)



        

    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,lista_plataformas)
    player_1.draw(screen)

   
    player_zombie.update(delta_ms,lista_plataformas)
    player_zombie.draw(screen)

    
# DIRECTION SE HACE NEGATIVO CUANDO SUBE EL PERSONAJE EN EL ASCENSOR, Y VA ESCALANDO
    
    for plataforma in lista_plataformas:
        if player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or player_1.rect_ground_collition.colliderect(plataforma.rect_top_collition):
            if plataforma.is_static is True: 
                #print("ES VERDADERO")
                player_1.move_y = 0 # Mover el personaje en la misma dirección que la plataforma
                plataforma.rect.y = plataforma.y_inicial
                
                
                
                #print(f"player rect y :{player_1.rect.y}")

        if player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or player_1.rect_ground_collition.colliderect(plataforma.rect_top_collition):
            
            if not plataforma.is_static:
                player_1.rect.y += plataforma.direction  # Mover el personaje en la misma dirección que la plataforma
                camera += 1
                print(f"direction {plataforma.direction}")
                #camera = player_1.rect.y - ALTO_VENTANA // 2
                #print("COLISION CON ASCENSOR")
                player_1.rect_ground_collition.y += plataforma.direction
    
            


    pygame.display.flip()
    

