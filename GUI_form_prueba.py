import sys
sys.path.append("C:/Users/navar/Desktop/UTN/juego_programacion/elevator_action_zombie/GUI/UI")  # Reemplaza 'ruta_completa_hacia_la_carpeta_UI' con la ruta absoluta hacia la carpeta UI

import pygame
from pygame.locals import *

from GUI.UI.GUI_button import *
from GUI.UI.GUI_slider import *
from GUI.UI.GUI_textbox import *
from GUI.UI.GUI_label import *
from GUI.UI.GUI_form import *
from GUI.UI.GUI_button_image import *
from GUI_form_menu_score import *
import sqlite3


    
class FormPrueba(Form):
    
    
    def __init__(self, screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
    
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        self.flag_play = True
        
        self.volumen = 0.10
                
        pygame.mixer.init()
        
        pygame.mixer.music.load("GUI/Recursos/sound_intro.wav")
        
        pygame.mixer.music.set_volume(self.volumen)
        
        pygame.mixer.music.play(-1)
        
        self.ejecutar_inicio = True
        self.ejecutar_menu = True
        self.ejecutar_juego = False
        
        self.nombre_jugador = None

        self.fondo = pygame.image.load("GUI/Recursos/fondo_menu_2.png").convert()
        self.fondo_scale = pygame.transform.scale(self.fondo, (0, 0))
        


        self.txt_nombre = TextBox(self._slave, x, y, 
                                  570, 30, 200, 50, 
                                  "gray","white","red","blue",2,
                                  "Comic Sans MS", 25, "black")
        
        self.btn_play = Button(self._slave, x, y, 120, 30,
                               200, 50,
                               "red", "orange", 
                               self. btn_play_click, "",
                               "Iniciar Partida", "Verdana",20, "orange"
                               )
        
        self.btn_play_2 = Button(self._slave, x, y, 350, 30,
                               200, 50,
                               "red", "orange", 
                               self. btn_play_click, "",
                               "Usuario", "Verdana",25, "orange"
                               )
        
        self.btn_play_3 = Button(self._slave, x, y, 790, 30,
                               200, 50,
                               "red", "orange", 
                               self. btn_play_click, "",
                               "Escenario", "Verdana",25, "orange"
                               )
        '''
        self.btn_play_4 = Button(self._slave, x, y, 940, 30,
                               200, 50,
                               "red", "orange", 
                               self. btn_play_click, "",
                               "Puntajes", "Verdana",25, "orange"
                               )
        '''
        
        self.slider_volumen = Slider(self._slave, x, y, 400,540, 500, 15, self.volumen, 
                                     "Red", "Orange")
        
        
        
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave,950,525, 80, 40, porcentaje_volumen,
                                   "Comic Sans MS", 10,"white", "GUI/Recursos/Table.png")
        
        
        self.btn_tabla = Button_Image(self._slave, x, y, 1010,30, 200, 50, "GUI/Recursos/boton_puntaje.png", 
                                      self.btn_tabla_click, "")
        
        
        
        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_play_2)
        self.lista_widgets.append(self.btn_play_3)
        #self.lista_widgets.append(self.btn_play_4)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)
        
    
    def render(self):
        self._slave.fill(self._color_background)        
        self._slave.blit(self.fondo, (0, 0)) 

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)#POLIMORFISMO
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        
    
    def btn_play_click(self, param):
        if self.flag_play:
            if param == "Iniciar Partida":
                print("EJECUTAR JUEGO")
                self.ejecutar_juego = True
                self.ejecutar_menu = False

            
            elif param == "Usuario":
                usuario_texto = self.txt_nombre.get_text()
                self.nombre_jugador = usuario_texto
                print(f"{self.nombre_jugador}")
            elif param == "Escenario":
            # Acción para el botón Play3
                print("PAUSE 3")
            elif param == "Puntajes":
            # Acción para el botón Play4
                print("PAUSE 4")
        
        self.flag_play = not self.flag_play
        
    
    def btn_tabla_click(self, param):
        
        conn = sqlite3.connect('tabla_puntuaciones.db')
        cursor = conn.cursor()

        cursor.execute("SELECT nombre_usuario, puntuacion FROM Puntuaciones ORDER BY puntuacion DESC LIMIT 5")
        records = cursor.fetchall()

        
        conn.close()         
        diccionario = [{"Jugador": jugador, "Score": score} for jugador, score in records]        
        nuevo_form = FormMenuScore(screen = self._master,
                                   x = 250,
                                   y = 25,
                                   w = 500,
                                   h = 550,
                                   color_background = "green",
                                   color_border = "gold",
                                   active = True,
                                   path_image = "GUI/Recursos/Window.png",
                                   scoreboard = diccionario,
                                   margen_x = 10,
                                   margen_y = 100,
                                   espacio = 10
                                   )

        self.show_dialog(nuevo_form)#Modal
