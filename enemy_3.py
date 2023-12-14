from doctest import FAIL_FAST
import pygame
from constants import *
from assistant import Auxiliar

pygame.init()
pygame.mixer.init()

class Enemy_zombie_tres:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,estado_inicial=None,recorrido=None,direction=None) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Walk_zombie_3.png",7,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Walk_zombie_3.png",7,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Idle_zombie_3.png",5,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Idle_zombie_3.png",5,1,True)
        self.run_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Run_zombie_3.png",7,1)
        self.run_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Run_zombie_3.png",7,1,True)
        self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Dead_zombie_3.png",5,1)
        self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Dead_zombie_3.png",5,1,True)
        self.attack_r = Auxiliar.getSurfaceFromSpriteSheet("zombies\Attack_zombie_3.png",4,1)
        self.attack_l = Auxiliar.getSurfaceFromSpriteSheet("zombies\Attack_zombie_3.png",4,1,True)
        self.is_attack = False
        
        self.attack_sound = pygame.mixer.Sound('Audio\soldier_herido.wav')
        self.attack_sound.set_volume(0.05)
        self.death_sound = pygame.mixer.Sound('Audio\enemy_down.wav')
        self.death_sound.set_volume(0.05)
        self.score_zombie = 100
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        
        self.recorrido_inicial = recorrido
        self.direction = direction
        self.recorrido = 0
        self.estado_inicial = estado_inicial
        self.estado_vida = True
        
        
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.camera = self.rect.y
        self.is_jump = False
        
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 5, GROUND_RECT_H)
        self.rect_top_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y+30, self.rect.w / 5, GROUND_RECT_H)
        self.rect_disparo = pygame.Rect(self.rect.x+10 + self.rect.w / 5, self.rect.y+30, self.rect.w / 2.5, 70)

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            if(self.direction == DIRECTION_L):
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
        
    def attack(self):
        if not (self.animation == self.attack_r or self.animation == self.attack_l):
            if self.direction == DIRECTION_R:
                self.animation = self.attack_r
                self.is_attack = False
            elif self.direction == DIRECTION_L:
                self.animation = self.attack_l
                self.is_attack = False
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            

    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if self.estado_vida:



                if self.animation == self.dead_r or self.animation == self.dead_l:
                    self.dead()
                
                if self.is_attack:
                    self.attack()
                else:                
                    if self.estado_inicial == "walk":            
                            self.recorrido += abs(self.direction)            
                                
                            if self.direction == 1 :
                                
                                    self.move_x = self.speed_walk
                                    self.animation = self.walk_r                
                                    self.add_x(self.move_x)
                                    self.add_y(self.move_y)
                                    if self.recorrido == self.recorrido_inicial or self.rect.x < 0:
                                        self.recorrido = 0
                                        self.direction = -1*self.direction               

                            if self.direction == -1 :  
                                
                                    self.move_x = -1*self.speed_walk
                                    self.animation = self.walk_l
                                    self.add_x(self.move_x)
                                    self.add_y(self.move_y)
                                    if self.recorrido == self.recorrido_inicial or self.rect.x < 0:
                                        self.recorrido = 0
                                        self.direction = -1*self.direction

                    if self.estado_inicial == "run":            
                            self.recorrido += abs(self.direction)            
                            if self.direction == DIRECTION_R:
                                self.move_x = self.speed_run
                                self.animation = self.run_r                
                                self.add_x(self.move_x)
                                self.add_y(self.move_y)
                                if self.recorrido >= self.recorrido_inicial or self.rect.x < 0 :
                                    self.recorrido = 0
                                    self.direction = -1*self.direction               

                            if self.direction == DIRECTION_L:                
                                self.move_x = -1*self.speed_run
                                self.animation = self.run_l
                                self.add_x(self.move_x)
                                self.add_y(self.move_y)
                                if self.recorrido >= self.recorrido_inicial or self.rect.x < 0 :
                                    self.recorrido = 0
                                    self.direction = -1*self.direction

                            
                    if self.estado_inicial == "stay":
                            self.stay()            


                    if(self.is_on_platform(lista_plataformas) == False):
                        self.add_y(self.gravity)

                #print(f"{self.direction}     {self.recorrido}    {self.frame}")
            
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= 540):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or self.rect_ground_collition.colliderect(plataforma.rect_top_collition)):
                    retorno = True
                    break   
        return retorno

    def dead(self):
        
        if self.animation != self.dead_r and self.animation != self.dead_l:
            if self.direction == DIRECTION_R:
                self.animation = self.dead_r
                self.move_x = 0
                self.frame = 0
                #self.state_colittion = False
                self.death_sound.play()
            if self.direction == DIRECTION_L:
                self.animation = self.dead_l
                self.move_x = 0
                self.frame = 0
                #self.state_colittion = False
                self.death_sound.play()
        self.estado_vida = False

                           
    def add_x(self,delta_x):
        self.rect.x += delta_x
        #print(f"{self.rect.x}")
        #print(f"ahora acaaaaa")
        self.rect_ground_collition.x += delta_x
        self.rect_top_collition.x += delta_x
        self.rect_disparo.x += delta_x  

    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y
        self.rect_top_collition.y += delta_y
        self.rect_disparo.y += delta_y



    def do_animation(self,delta_ms):
        if not self.animation in (self.dead_r, self.dead_l):
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1
                else: 
                    self.frame = 0
        else:
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1



    def update(self,delta_ms,lista_plataformas):
        if not self.animation == self.dead_r or not self.animation == self.dead_l:
            self.do_movement(delta_ms,lista_plataformas)
            self.do_animation(delta_ms)   
        
    
    def draw(self,screen):
        if(DEBUG):            
            pygame.draw.rect(screen,RED,self.rect)
            
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            pygame.draw.rect(screen,GREEN,self.rect_top_collition)
            pygame.draw.rect(screen,YELLOW,self.rect_disparo)
            
        
        if self.animation in (self.dead_r, self.dead_l):
            self.image = self.animation[self.frame]
        else:
            self.image = self.animation[self.frame]

        screen.blit(self.image, self.rect)
    