from doctest import FAIL_FAST
import pygame
from constants import *
from assistant import Auxiliar
from moviepy.editor import VideoFileClip

class Municion:
    def __init__(self,x,y):
        self.municion = 5
        self.image_municion = pygame.image.load("proyectil/recarga.png")
        self.image_municion = pygame.transform.scale(self.image_municion, (30,30))
        self.rect_municion = self.image_municion.get_rect()
        self.rect_municion.x = x
        self.rect_municion.y = y
        self.municion_sound = pygame.mixer.Sound('Audio/recharge.wav')

    def draw(self,screen):
        screen.blit(self.image_municion, self.rect_municion)

    def play_sound(self):
        self.municion_sound.play()

class Coins:
    def __init__(self,x,y):
        self.score_coins = 1000
        self.image_coins = pygame.image.load("proyectil/coin_2.png")
        self.image_coins = pygame.transform.scale(self.image_coins, (40,40))
        self.rect_coins = self.image_coins.get_rect()
        self.rect_coins.x = x
        self.rect_coins.y = y
        self.sound_coins = pygame.mixer.Sound('Audio\sound_coins.wav')

    def draw(self,screen):
        screen.blit(self.image_coins, self.rect_coins)

    def play_sound(self):
        self.sound_coins.play()

class victory:
    def __init__(self,x,y):   
        
        self.sound_victory = pygame.mixer.Sound('Audio\sound_coins.wav')
        self.font = pygame.font.Font("fonts\slkscre.ttf", 15) 
        self.text_victory = self.font.render(f"NEXT LEVEL", True, (255, 255, 255))
        self.text_rect = self.text_victory.get_rect()
        self.text_rect.x = x
        self.text_rect.y = y
        self.video_victoria_path = 'video/victoria_helicoptero.mpeg' 
        self.video_victoria = VideoFileClip(self.video_victoria_path)
        self.video_victoria = self.video_victoria.volumex(0.2)
        self.victoria_stage_01 = False
    
    def draw(self,screen):
        screen.blit(self.text_victory, self.text_rect)

    def play_victory_video(self):
        if self.victoria_stage_01:
            self.video_victoria.preview()
            self.victoria_stage_01 = False


class Disparo:
    def __init__(self, x, y, direccion):
        self.superficie = pygame.image.load("proyectil/bala.png")
        #self.superficie = pygame.transform.scale(self.superficie, (10,10))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

    def actualizar(self, screen):
        if self.direccion == "Derecha":
            self.rectangulo.x += 70

        elif self.direccion == "Izquierda":
            self.rectangulo.x -= 70
            self.superficie = pygame.transform.flip(self.superficie,True,False)
        
        
        screen.blit(self.superficie, self.rectangulo)
        #pygame.draw.rect(screen,RED,self.rectangulo)
        #surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)

    

    