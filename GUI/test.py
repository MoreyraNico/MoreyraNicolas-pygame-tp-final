import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba
from moviepy.editor import VideoFileClip
from pygame.locals import *

pygame.init()
pygame.mixer.init()
WIDTH = 1300
HEIGHT = 650
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))


video_path = "GUI\Recursos\presentacion.mpeg"  # Reemplaza con la ruta de tu video
video = VideoFileClip(video_path)

# Duración del video en segundos
video_duration = video.duration

# Iniciar reproducción del video
#video.preview()
#pygame.mixer.music.load('GUI/Recursos/sound_intro.wav')
#pygame.mixer.music.play(-1)


form_prueba = FormPrueba(pantalla,0,0, 1300, 650,"black", "black", 5, True) # 01 creo el objeto form prueba


while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            pygame.mixer.music.stop()
            sys.exit()

    pantalla.fill("Black")
    
    #if video.duration <= video_duration:
    form_prueba.update(eventos)

    pygame.display.flip()