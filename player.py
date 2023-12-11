from doctest import FAIL_FAST
import pygame
from moviepy.editor import VideoFileClip
from constants import *
from assistant import Auxiliar
from disparo import Disparo


pygame.init()
pygame.mixer.init()



class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,state_colittion = None) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Run.png",6,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Run.png",6,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Idle.png",7,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Idle.png",7,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/jump.png",11,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/jump.png",11,1,True)
        self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Dead.png",5,1)
        self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Dead.png",5,1,True)
        self.shoot_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Attacck.png",5,1)
        self.shoot_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Attacck.png",5,1,True)
        self.shoot_down_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Shot_2.png",4,1)
        self.shoot_down_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Shot_2.png",4,1,True)
        self.shoot_recharge_r = Auxiliar.getSurfaceFromSpriteSheet("soldier/Recharge.png",8,1)
        self.shoot_recharge_l = Auxiliar.getSurfaceFromSpriteSheet("soldier/Recharge.png",8,1,True)
        
        self.disparo_sound = pygame.mixer.Sound('Audio/disparo.wav')
        self.disparo_sin_balas = pygame.mixer.Sound('Audio/sin_balas.wav')
        
        
        
        self.death_sound = pygame.mixer.Sound('Audio\death_soldier.wav')
        self.video_muerte_path = 'video/muerte_juego.avi'  # Ruta de tu archivo de video
        self.video_muerte = VideoFileClip(self.video_muerte_path)
        self.is_playing_video = False
        self.death_time = 0
        self.current_time = 0
        self.is_dead = False
        self.damage_max = 120
        self.damage_recibido = 0
        self.frame = 0
        
        self.lives = 2
        self.lives_count = 0
        self.vida = True
        self.score = 0
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.state_colittion = True

        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]

        self.lista_balas = []
        self.max_shoots = 5  
        self.shoot_count = 0   
        self.state_recharge = True 
        
        self.is_jump = False
        self.y_start_jump = 0
        self.jump_height = jump_height
        
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms       

        self.rect = self.image.get_rect()
        self.x_inicial = x
        self.y_inicial = y

        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 5, GROUND_RECT_H)
        self.rect_top_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y+60, self.rect.w / 8, 5)
        self.rect_disparo = pygame.Rect(self.rect.x+15 + self.rect.w / 5, self.rect.y+60, self.rect.w / 6, 70)


    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                '''
                if self.rect.x < 0 and self.rect_ground_collition.x <= 42 and self.rect_disparo.x <= 40 and self.rect_top_collition.x <= 42 :
                    self.rect.x = 0
                '''
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                '''
                if self.rect.x < 0 and self.rect_ground_collition.x <= 42 and self.rect_disparo.x <= 40 and self.rect_top_collition.x <= 42:
                    self.rect.x = 0
                '''
        #print(f"{self.rect.x}   {self.rect_ground_collition.x}     {self.rect_disparo.x}   {self.rect_top_collition.x}")
                
        

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

    def recharge(self):
        if self.state_recharge:
            if(self.animation != self.shoot_recharge_r and self.animation != self.shoot_recharge_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_recharge_r
                    self.recharge_sound.play()
                    self.state_recharge = False
                else:
                    self.animation = self.shoot_recharge_l
                    self.recharge_sound.play()
                    self.state_recharge = False
                self.move_x = 0
                self.move_y = 0
                self.frame = 0
        
            

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def dead(self,damage_recibido):
        
            self.damage_recibido += damage_recibido
            if self.damage_recibido > self.damage_max:
                if self.animation != self.dead_r and self.animation != self.dead_l:
                    if self.direction == DIRECTION_R:
                        self.animation = self.dead_r
                        self.move_x = 0
                        self.frame = 0
                        #self.state_colittion = False
                        self.death_sound.play()
                        self.vida = False
                        self.is_dead = True
                        self.death_time = pygame.time.get_ticks()
                        
                    else:
                        self.animation = self.dead_l
                        self.move_x = 0
                        self.frame = 0
                        self.death_sound.play()
                        self.vida = False
                        self.is_dead = True
                        self.death_time = pygame.time.get_ticks()
    
    def revive(self):
            # Restablece la posición del jugador y otros atributos al morir
            self.damage_recibido = 0
            self.rect.x = 0
            self.rect_ground_collition.x = 42
            self.rect_top_collition.x = 42
            self.rect_disparo.x = 40
            self.rect.y = 500
            self.rect_ground_collition.y = 623
            self.rect_top_collition.y = 560
            self.rect_disparo.y = 560
            
            self.vida = True
            self.is_dead = False
            self.stay()
        

    def shoot(self):
        if self.animation != self.shoot_r and self.animation != self.shoot_r:
            if self.direction == DIRECTION_R:
                self.animation = self.shoot_r
                self.move_x = 0
                self.frame = 0
            else:
                self.animation = self.shoot_l
                self.move_x = 0
                self.frame = 0
                
    def shoot_down(self):
        if self.animation != self.shoot_down_r and self.animation != self.shoot_down_l:
            if self.direction == DIRECTION_R:
                self.animation = self.shoot_down_r
                self.move_x = 0
                self.frame = 0
            else:
                self.animation = self.shoot_down_l
                self.move_x = 0
                self.frame = 0


    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            
            self.add_x(self.move_x)
            self.add_y(self.move_y)

            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)
            elif(self.is_jump): # SACAR
                if self.rect.y <= self.y_start_jump - self.jump_height:
                    self.is_jump = False
                else:
                    self.add_y(self.move_y)
                    self.is_jump = False
                    

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
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)

        if self.is_dead:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.death_time >= 3000:
                if self.lives_count <= self.lives:   # 3000 ms = 3 segundos
                    self.lives_count += 1
                    self.revive()  # Llama a la función revive cuando ha pasado el tiempo después de la muerte

                    # Restablece los estados después de revivir
                    self.vida = True
                    self.is_dead = False
                    #self.stay() 
                else:
                    self.video_muerte.preview()
                    self.lives_count=0

    def play_death_video(self):
        if not self.is_playing_video:
            self.is_playing_video = True
            self.video_muerte.preview()
            
            

        
    
    def draw(self,screen):
        if(DEBUG):            
            #pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,YELLOW,self.rect_disparo)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            pygame.draw.rect(screen,GREEN,self.rect_top_collition)
            
            
        if self.animation in (self.dead_r, self.dead_l):
            self.image = self.animation[self.frame]
        else:
            self.image = self.animation[self.frame]

        screen.blit(self.image, self.rect)

        

    def events(self,delta_ms,keys,screen):
        if self.vida and not self.is_dead:
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_L)
            if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_R)
            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()
                
            if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()   
            if(keys[pygame.K_SPACE]):
                self.jump(True)
            if(keys[pygame.K_d]):
                self.dead()
            if(keys[pygame.K_s]):
                self.shoot()
            if(keys[pygame.K_DOWN]) and (keys[pygame.K_s]) :
                self.shoot_down()
            #if(keys[pygame.K_r]):
                #self.recharge()

        else:
            #print(f"MUERTE EN EVENTS")
            self.dead(0)

        self.actualizar_balas(screen)

    def lanzar_bala(self):##########################################################################################
        x = None
        y = self.rect_disparo.centery -5
        if self.animation == self.shoot_r or self.animation == self.shoot_down_r :
            x = self.rect_disparo.right-80
            direccion_bala = "Derecha"
            #RECARGAS
            if self.shoot_count < self.max_shoots:
                self.disparo_sound.play()
            else:
                self.disparo_sin_balas.play()

        elif self.animation == self.shoot_l or self.animation == self.shoot_down_l :
            x = self.rect_disparo.left+80
            direccion_bala = "Izquierda"
            #RECARGAS
            if self.shoot_count < self.max_shoots:
                self.disparo_sound.play()
            else:
                self.disparo_sin_balas.play()
            
    
        if x is not None:
            if self.shoot_count < self.max_shoots:  # Verifica si no se excede el límite
                self.lista_balas.append(Disparo(x, y, direccion_bala))
                self.shoot_count += 1 
    
    def actualizar_balas(self, screen):
        i = 0
        while i < len(self.lista_balas):
            bala = self.lista_balas[i]
            bala.actualizar(screen)
            if bala.rectangulo.centerx < 0 or bala.rectangulo.centerx > ANCHO_VENTANA:
                self.lista_balas.pop(i)
                i -= 1
            i += 1
        



    