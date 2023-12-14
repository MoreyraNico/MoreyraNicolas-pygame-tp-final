import pygame
from constants import *
import sys
import sqlite3



def draw_game_screen(screen, game_time,damage_recibido,shoot_count,max_shoots,lives_count,score,nombre_usuario):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, ANCHO_VENTANA, 55))

    font = pygame.font.Font("fonts\slkscre.ttf", 20)  
    text_shoots = font.render(f"SHOOTS: {shoot_count} / {max_shoots}", True, (255, 255, 255))
    text_vida = font.render(f"Life: {lives_count}-3 / Score: {score}", True, (255, 255, 255))
    text_name = font.render(f":{nombre_usuario}", True, (255, 255, 255))
    screen.blit(text_shoots, (1050, 5))
    screen.blit(text_vida, (950, 30))
    
    
    damage_recibido = int(damage_recibido)
    if damage_recibido < 30:
        health_bar = pygame.image.load("health_bar/health_bar_5.png")
        print("30")
    elif damage_recibido < 60:
        health_bar = pygame.image.load("health_bar/health_bar_4.png")
        print("60")
    elif damage_recibido < 90:
        health_bar = pygame.image.load("health_bar/health_bar_3.png")
        print("90")
    elif damage_recibido < 120:
        health_bar = pygame.image.load("health_bar/health_bar_2.png")
        print("120")
    else:
        health_bar = pygame.image.load("health_bar/health_bar_1.png")
        print("resto")

    health_bar = pygame.transform.scale(health_bar, (400, 60))
    screen.blit(health_bar, (0, 0))

    font = pygame.font.Font("fonts\slkscre.ttf", 45)  
    time_str = format_time(game_time)
    text_time = font.render(f"TIME {time_str}", True, (255, 255, 255))
    screen.blit(text_time, (490, 5)) 
    screen.blit(text_name, (220, 14)) 
'''
def draw_victory(screen):
    
    font = pygame.font.Font("fonts\slkscre.ttf", 20)  # Fuente y tamaño del texto ajustable
    text_victory = font.render(f"NEXT LEVEL", True, (255, 255, 255))
    text_rect = text_victory.get_rect()  
    screen.blit(text_victory,text_rect(500, 550))
'''  

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def draw_pause(screen):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, ANCHO_VENTANA, 55))

    font = pygame.font.Font("fonts\slkscre.ttf", 30)  
    text_pause = font.render(f"PAUSE", True, (255, 255, 255))
    text_menu = font.render(f"Volver al menu principal", True, (255, 255, 255))
    text_salir = font.render(f"Salir del juego", True, (255, 255, 255))

    screen.blit(text_pause, (550, 200))
    screen.blit(text_menu, (400, 300))
    screen.blit(text_salir, (450, 400))

def click(event, pausa):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        
        button_rect = pygame.Rect(550, 300, 100, 100)
        button_rect_exit = pygame.Rect(550, 400, 100, 100)
        if button_rect.collidepoint(mouse_pos):
            pausa = False  
        elif button_rect_exit.collidepoint(mouse_pos):
            pygame.quit()  
            sys.exit()

    return pausa

def creacion_bd():
    
    conexion = sqlite3.connect("tabla_puntuaciones.db")    
    conexion.execute('''CREATE TABLE IF NOT EXISTS Puntuaciones (
                            nombre_usuario TEXT,
                            puntuacion INTEGER
                        )''')    
    conexion.commit()
    conexion.close()

    