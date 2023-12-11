import pygame
from constants import *



def draw_game_screen(screen, game_time,damage_recibido,shoot_count,max_shoots,lives_count,score):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, ANCHO_VENTANA, 55))

    font = pygame.font.Font("fonts\slkscre.ttf", 20)  
    text_shoots = font.render(f"SHOOTS: {shoot_count} / {max_shoots}", True, (255, 255, 255))
    text_vida = font.render(f"Life: {lives_count}-3 / Score: {score}", True, (255, 255, 255))
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