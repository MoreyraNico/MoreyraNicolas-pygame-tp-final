from doctest import FAIL_FAST
import pygame
from constants import *
from assistant import Auxiliar

class Enemy_zombie_uno:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,estado_inicial=None,recorrido=None,direction=None) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Walk_zombie_1.png",10,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Walk_zombie_1.png",10,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Idle_zombie_1.png",9,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Idle_zombie_1.png",9,1,True)
        self.run_r = Auxiliar.getSurfaceFromSpriteSheet("zombies/Run_zombie_1.png",8,1)
        self.run_l = Auxiliar.getSurfaceFromSpriteSheet("zombies/Run_zombie_1.png",8,1,True)
        #self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/soldier/jump.png",11,1)
        #self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/soldier/jump.png",11,1,True)
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
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
        
    '''
    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):

                self.move_x = self.speed_walk
                self.animation = self.walk_r
                
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
        
    '''
    '''
    def jump(self,on_off = True):
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    '''

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0
            
            print(f"{self.rect.x}")

            if self.rect.x > 0:
                if self.estado_inicial == "walk":            
                    self.recorrido += abs(self.direction)            
                        
                    if self.direction == 1 :
                        
                            self.move_x = self.speed_walk
                            self.animation = self.walk_r                
                            self.add_x(self.move_x)
                            self.add_y(self.move_y)
                            if self.recorrido == self.recorrido_inicial:
                                self.recorrido = 0
                                self.direction = -1*self.direction               

                    if self.direction == -1 :  
                        
                            self.move_x = -1*self.speed_walk
                            self.animation = self.walk_l
                            self.add_x(self.move_x)
                            self.add_y(self.move_y)
                            if self.recorrido == self.recorrido_inicial:
                                self.recorrido = 0
                                self.direction = -1*self.direction

                if self.estado_inicial == "run":            
                    self.recorrido += abs(self.direction)            
                    if self.direction > 0:
                        self.move_x = self.speed_run
                        self.animation = self.run_r                
                        self.add_x(self.move_x)
                        self.add_y(self.move_y)
                        if self.recorrido == self.recorrido_inicial :
                            self.recorrido = 0
                            self.direction = -1*self.direction               

                    if self.direction == -1:                
                        self.move_x = -1*self.speed_run
                        self.animation = self.run_l
                        self.add_x(self.move_x)
                        self.add_y(self.move_y)
                        if self.recorrido == self.recorrido_inicial :
                            self.recorrido = 0
                            self.direction = -1*self.direction

                    
                elif self.estado_inicial == "stay":
                    self.stay()
            
            elif self.rect.x < 0 or self.recorrido == self.recorrido_inicial :
                self.direction = -1*self.direction
                if self.direction > 0:
                        self.move_x = self.speed_run
                        self.animation = self.run_r                
                        self.add_x(self.move_x)
                        self.add_y(self.move_y)
                        if self.recorrido == self.recorrido_inicial :
                            self.recorrido = 0
                            self.direction = -1*self.direction               

                if self.direction == -1:                
                        self.move_x = -1*self.speed_run
                        self.animation = self.run_l
                        self.add_x(self.move_x)
                        self.add_y(self.move_y)
                        if self.recorrido == self.recorrido_inicial :
                            self.recorrido = 0
                            self.direction = -1*self.direction




                # Imprime la dirección actual para verificar si cambia correctamente
                
                '''
                if self.direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                '''

            #self.add_x(self.move_x)
            #self.add_y(self.move_y)

            '''
            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)
            
            elif(self.is_jump): # SACAR
                if self.rect.y <= self.y_start_jump - self.jump_height:
                    self.is_jump = False
                else:
                    self.add_y(self.move_y)
                    self.is_jump = False
            '''        

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition) or self.rect_ground_collition.colliderect(plataforma.rect_top_collition)):
                    retorno = True
                    break   
        return retorno


                           
    def add_x(self,delta_x):
        self.rect.x += delta_x
        #print(f"{self.rect.x}")
        #print(f"ahora acaaaaa")
        self.rect_ground_collition.x += delta_x        

    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0



    def update(self,delta_ms,lista_plataformas):
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)

    
        
    
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

        
    
    #def events(self,delta_ms):
        #if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
        #    self.walk(DIRECTION_L)
        #if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            #self.walk(DIRECTION_R)
        #if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
        #    self.stay()
        #if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
        #    self.stay()   
        #if(keys[pygame.K_SPACE]):
        #    self.jump(True)
    