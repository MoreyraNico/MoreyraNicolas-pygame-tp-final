import pygame
import sys
from constants import *
from player import Player
from plataforma import *
from enemy import Enemy_zombie_uno
from enemy_2 import Enemy_zombie_dos
from enemy_3 import Enemy_zombie_tres
from enemy_4 import Enemy_zombie_cuatro
from disparo import *   
from draws_utils import *
from FormMenu import *


pygame.init()
pygame.mixer.init()


clock = pygame.time.Clock()
reloj_menu = pygame.time.Clock()
game_time = 0
delta_time = 0
pygame.mixer.music.load('Audio/ambient.wav')
pygame.mixer.music.play(-1)

ambient_zombie_sound = pygame.mixer.Sound('Audio/ambient_zombie.wav')
ambient_zombie_sound.play(-1)

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
imagen_fondo = pygame.image.load("stage/stage_map_3.png")


player_1 = Player(x=0,y=500,speed_walk=8,speed_run=8,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,state_colittion=True)
victoria_stage_1 = victory(x=1050,y=100)
lista_enemigos = []
lista_enemigos.append(Enemy_zombie_dos(x=100,y=540,speed_walk=3,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="run",recorrido=25, direction = 1))
lista_enemigos.append(Enemy_zombie_tres(x=400,y=540,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="run",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_dos(x=20,y=GROUND_LEVEL_5,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_dos(x=900,y=80,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_dos(x=1150,y=GROUND_LEVEL_3,speed_walk=4,speed_run=6,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay",recorrido=15, direction = 1))
lista_enemigos.append(Enemy_zombie_dos(x=1050,y=GROUND_LEVEL_4,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_dos(x=1050,y=GROUND_LEVEL_5,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_tres(x=400,y=80,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_tres(x=1150,y=GROUND_LEVEL_2,speed_walk=4,speed_run=6,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay",recorrido=15, direction = 1))
lista_enemigos.append(Enemy_zombie_tres(x=20,y=GROUND_LEVEL_2,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk",recorrido=30, direction = 1))
lista_enemigos.append(Enemy_zombie_tres(x=750,y=80,speed_walk=4,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay",recorrido=30, direction = 1))
# HORDA DE ZOMBIES
lista_enemigos.append(Enemy_zombie_dos(x=600,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="stay", recorrido=0,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1160,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1130,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1110,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1080,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1050,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1500,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1470,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1440,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1410,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1380,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1350,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1320,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1290,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1260,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1230,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1530,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_dos(x=1560,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1590,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1620,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1650,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1680,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))
lista_enemigos.append(Enemy_zombie_tres(x=1710,y=540,speed_walk=1,speed_run=4,gravity=8,jump_power=10,frame_rate_ms=60,move_rate_ms=50,jump_height=10,estado_inicial="walk", recorrido=450,direction =-1))

lista_coins = []
lista_coins.append(Coins(x=400,y=550))
lista_coins.append(Coins(x=100,y=210))
lista_coins.append(Coins(x=100,y=310))

lista_municiones = []
lista_municiones.append(Municion(x=200,y=550))
lista_municiones.append(Municion(x=50,y=210))
lista_municiones.append(Municion(x=50,y=310))

lista_plataformas = []
lista_plataformas.append(Platform(553,45,130,130,recorrido_limite=460,velocidad=2))#Ascensor Principal
lista_plataformas.append(Platform(228,45,130,130,recorrido_limite=350,velocidad=2))#Ascensor 02
lista_plataformas.append(Platform(390,45,130,130,recorrido_limite=350,velocidad=2))#Ascensor 03
lista_plataformas.append(Platform(715,45,130,130,recorrido_limite=350,velocidad=2))#Ascensor 04
lista_plataformas.append(Platform(878,45,130,130,recorrido_limite=350,velocidad=2))#Ascensor 05

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

recorrido_muerte = 0
contador_recorrido_muerte = 0
contador_recorrido_muerte_2 = 0
dead = None
bandera = True

recorrido_muerte_zombie = 0
contador_recorrido_muerte_zombie = 0
contador_recorrido_muerte_2_zombie = 0
bandera_zombie = True

disparo = Disparo(0,0,0)
flag_disparo = False
tiempo_ultimo_disparo = 0

balas_a_eliminar = []

bandera_victoria = True

ejecutar_menu = True
ejecutar_game = False

form_prueba = FormPrueba(screen,200,100, 900, 350,"black", "blue", 5, True)

while ejecutar_menu:
    reloj_menu.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    form_prueba.update(eventos)
    pygame.display.flip()
    

while ejecutar_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.music.stop()
            
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    delta_ms = clock.tick(FPS)
    delta_time += delta_ms
    if delta_time >= 1000:  
        game_time += 1
        delta_time = 0
    
    porcion_fondo = imagen_fondo.subsurface((0, 1530, 320, 320))
    porcion_fondo = pygame.transform.scale(porcion_fondo,(ANCHO_VENTANA,ALTO_VENTANA))    
    screen.blit(porcion_fondo,(0, 0))    
    
    draw_game_screen(screen, game_time,player_1.damage_recibido, player_1.shoot_count, player_1.max_shoots,player_1.lives_count,player_1.score)
    

    #lista_plataformas = creacion_plataformas()
    for plataforma in lista_plataformas:
        plataforma.update()        
        plataforma.draw(screen)

    for coin in lista_coins:
        coin.draw(screen)

    for municion in lista_municiones:
        municion.draw(screen)    
    
    for enemy in lista_enemigos:
        enemy.update(delta_ms,lista_plataformas)
        enemy.draw(screen)    
    
    player_1.events(delta_ms,keys,screen)
    player_1.update(delta_ms,lista_plataformas)
    player_1.draw(screen)

    # MOVIMIENTOS / DISPARO
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_RIGHT]):
        flag_disparo = True
    elif(keys[pygame.K_LEFT]):
        flag_disparo = True
    elif(keys[pygame.K_SPACE]):        
        flag_disparo = True
    else:
        flag_disparo = True

    # DISPARO###########################################################
    if flag_disparo and keys[pygame.K_s]:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_ultimo_disparo >= 200:
            player_1.lanzar_bala()
            flag_disparo = False
            tiempo_ultimo_disparo = tiempo_actual
    
    
    ######### SOLDIER MUERTE POR CAIDA ##########################################################################################
    for plataforma in lista_plataformas:
        if player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
            if bandera:
                recorrido_muerte = player_1.rect.y
                bandera = False

    if bandera is False:
        contador_recorrido_muerte = player_1.rect.y - recorrido_muerte
        recorrido_muerte = player_1.rect.y

    if contador_recorrido_muerte == 8:
        contador_recorrido_muerte_2 += contador_recorrido_muerte
    
    for plataforma in lista_plataformas:
        if contador_recorrido_muerte_2 > 80:
            if player_1.rect_ground_collition.colliderect(plataforma.rect_top_collition) or player_1.rect.y >= 500 :
                contador_recorrido_muerte = 0
                contador_recorrido_muerte_2 = 0
                recorrido_muerte = 0
                player_1.dead(120)#######################################################
                #print("MUERTE POR CAIDA")
    
    #print(f"{player_1.rect.y}   {recorrido_muerte}   {contador_recorrido_muerte}   {contador_recorrido_muerte_2}")
    ####################################################################################################################
    
    ######## MUERTE POR CAIDA ZOMBIE ###################################################################################
    for plataforma in lista_plataformas:
        for enemy in lista_enemigos:
            if enemy.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                if bandera_zombie:
                    recorrido_muerte_zombie = enemy.rect.y
                    bandera_zombie = False
    for enemy in lista_enemigos:
        if bandera_zombie is False:
            contador_recorrido_muerte_zombie = enemy.rect.y - recorrido_muerte
            recorrido_muerte_zombie = enemy.rect.y

        if contador_recorrido_muerte_zombie == 8:
            contador_recorrido_muerte_2_zombie += contador_recorrido_muerte_zombie
        
    for plataforma in lista_plataformas:
        if contador_recorrido_muerte_2_zombie > 80:
            if enemy.rect_ground_collition.colliderect(plataforma.rect_top_collition) or enemy.rect.y >= 500 :
                #print("COLISIONOO")
                enemy.dead()
    ####################################################################################################################

    ########################## MUERTE POR APLASTAMIENTO, Y SUBIR ASCENSOR ###############################################
    for plataforma in lista_plataformas:
        if plataforma.tope is True:
            if player_1.rect_top_collition.colliderect(plataforma.rect_top_collition):            
                player_1.dead(120)##########################################################
                #print("MUERTE POR APLASTAMIENTO LINEA SUPERIOR")
        if plataforma.is_static is not True: 
            if player_1.rect_top_collition.colliderect(plataforma.rect_ground_collition):
                player_1.dead(120)########################################################
                dead = True
                #print("MUERTE POR APLASTAMIENTO CON BASE ASCENSOR")

       
    #print(player_1.state_colittion)
    #if dead is not True:
        for plataforma in lista_plataformas:
            if player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or player_1.rect_ground_collition.colliderect(plataforma.rect_top_collition):
                if plataforma.is_static is True: 
                    player_1.move_y = 0 # Mover el personaje en la misma dirección que la plataforma
                    plataforma.rect.y = plataforma.y_inicial

            if player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or player_1.rect_ground_collition.colliderect(plataforma.rect_top_collition):            
                if not plataforma.is_static:
                    player_1.rect.y += plataforma.direction * plataforma.velocidad  # Mover el personaje en la misma dirección que la plataforma
                    player_1.rect_ground_collition.y += plataforma.direction * plataforma.velocidad
                    player_1.rect_top_collition.y += plataforma.direction * plataforma.velocidad
                    player_1.rect_disparo.y += plataforma.direction * plataforma.velocidad                    
    #else:
        #pass
    ######################################################################################################################
    


    ############## ZOMBIE SUBE ASCENSOR y muerte por aplastamiento ##########################################################
    for plataforma in lista_plataformas:
        for enemy in lista_enemigos:
            if plataforma.tope is True:
                if enemy.rect_top_collition.colliderect(plataforma.rect_top_collition):            
                    enemy.dead()
            if plataforma.is_static is not True: 
                if enemy.rect_top_collition.colliderect(plataforma.rect_ground_collition):
                    enemy.dead()
                    dead_zombie = True
    
    

    for plataforma in lista_plataformas:
        for enemy in lista_enemigos:
            if enemy.rect.y < 540:
                
                    if enemy.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or enemy.rect_ground_collition.colliderect(plataforma.rect_top_collition) or enemy.rect_disparo.colliderect(plataforma.rect_top_collition):
                        if plataforma.is_static is True: 
                            enemy.move_y = 0 # Mover el personaje en la misma dirección que la plataforma
                            #print(f"{enemy.rect.y}")
                            

                    if enemy.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or enemy.rect_ground_collition.colliderect(plataforma.rect_top_collition) or enemy.rect_disparo.colliderect(plataforma.rect_top_collition):          
                        if not plataforma.is_static:
                            enemy.rect.y += plataforma.direction * plataforma.velocidad  # Mover el personaje en la misma dirección que la plataforma
                            enemy.rect_ground_collition.y += plataforma.direction * plataforma.velocidad
                            enemy.rect_top_collition.y += plataforma.direction * plataforma.velocidad
                            enemy.rect_disparo.y += plataforma.direction * plataforma.velocidad
                            #print(f"{enemy.rect.y}")

    #####################################################################################################                    
                        
    
    ##################### MUERTE POR TOCAR ENEMIGO ########################################################
    for plataforma in lista_plataformas:
            for enemy in lista_enemigos:
                if enemy.estado_vida:
                    if enemy.rect_disparo.colliderect(player_1.rect_ground_collition):
                        enemy.is_attack = True
                        enemy.attack()
                        player_1.dead(0.1)
                    else:
                        enemy.is_attack = False
                    if player_1.is_dead:
                        enemy.is_attack = False

                        
                        #print("MUERTE POR TOCAR ENEMIGO") 
    ########################################################################################################
    
    for bala in player_1.lista_balas:
        for enemy in lista_enemigos:
            if enemy.estado_vida and bala.rectangulo.colliderect(enemy.rect_disparo):
                enemy.dead()
                player_1.score += enemy.score_zombie
                balas_a_eliminar.append(bala)
    
    for bala in balas_a_eliminar:
        if bala in player_1.lista_balas:
            player_1.lista_balas.remove(bala)

    for municion in lista_municiones:
        if player_1.rect_disparo.colliderect(municion.rect_municion):
            #print(f"TOCO LA MUNICION")
            player_1.max_shoots += municion.municion
            lista_municiones.remove(municion)
            municion.municion_sound.play()
            player_1.state_recharge = True

    if not lista_coins:
        victoria_stage_1.draw(screen)
        if bandera_victoria:
            if player_1.rect_disparo.colliderect(victoria_stage_1.text_rect):
                print("GANASTE")
                victoria_stage_1.victoria_stage_01 = True
                victoria_stage_1.play_victory_video()
                bandera_victoria = False

    else:
        for coin in lista_coins:
            if player_1.rect_disparo.colliderect(coin.rect_coins):
                coin.play_sound()
                player_1.score += coin.score_coins
                lista_coins.remove(coin)
            
    
    pygame.display.flip()
    

