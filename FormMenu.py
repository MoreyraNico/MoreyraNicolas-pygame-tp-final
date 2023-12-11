import pygame
from pygame.locals import *
'''
from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
'''

    
class FormPrueba():    
    def __init__(self,screen, x,y,w,h,color_background = "Black", color_border = "Red", border_size = -1, active = True):
        self.master = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.border_size = border_size

        self.slave = None
        self.slave_rect = None        
        self.slave = pygame.Surface((w,h))
        self.slave_rect = self.slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None

        self.flag_play = True
        '''
        self.volumen = 0.2
                
        pygame.mixer.init()
        
        pygame.mixer.music.load("GUI/Recursos/Vengeance (Loopable).wav")
        
        pygame.mixer.music.set_volume(self.volumen)
        
        pygame.mixer.music.play(-1)
        '''

        '''
        self.txt_nombre = TextBox(self.slave, x, y, 
                                  50, 50, 150, 30, 
                                  "gray","white","red","blue",2,
                                  "Comic Sans MS", 15, "black")
        '''
        self.boton_play = Button(self.slave,
                                 x,y,
                                 100,100,
                                 100,50,
                                 "Red","Blue",
                                 self.btn_play_click, "Nombre", "Pausa",
                                 font="Verdana",font_color="Black",font_size=15)
        
        '''
        self.slider_volumen = Slider(self._slave, x, y, 100,200, 500, 15, self.volumen, 
                                     "blue", "white")
        
        
        
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave,650,190, 100, 50, porcentaje_volumen,
                                   "Comic Sans MS", 15,"white", "GUI/Recursos/Table.png")
        
        
        self.btn_tabla = Button_Image(self._slave, x, y, 225,100, 50, 50, "GUI/Recursos/Menu_BTN.png", 
                                      self.btn_tabla_click, "")
        
        
        '''
        #self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.boton_play)
        #self.lista_widgets.append(self.slider_volumen)
        #self.lista_widgets.append(self.label_volumen)
        #self.lista_widgets.append(self.btn_tabla)

    def draw(self):
        self.master.blit(self.slave,self.slave_rect)
        pygame.draw.rect(self.master, self.color_border, self.slave_rect, self.border_size)   


    
    
    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None
    




    
    def render(self):
        self.slave.fill(self.color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                #self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    '''
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    '''   
        
    
    # @staticmethod
    def btn_play_click(self, param):
        if self.flag_play:
           pygame.mixer.music.pause()
           self.boton_play.color_background = "Cyan"
           self.boton_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.boton_play.color_background = "Red"
            self.boton_play.set_text("Pause")
        self.flag_play = not self.flag_play
        
    '''
    def btn_tabla_click(self, param):
        diccionario = [{"Jugador": "Mario", "Score": 100},
                       {"Jugador": "Gio", "Score": 150},
                       {"Jugador": "Uriel", "Score": 250}]
        
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
    '''

class Button():
    def __init__(self, screen,master_x,master_y, x,y,w,h,color_background,color_border, onclick, onclick_param, text, font, font_size, font_color):
        self.master = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        
        pygame.font.init()
        self.onclick = onclick
        self.onclick_param = onclick_param
        self.text = text
        self.font = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.master_x = master_x
        self.master_y = master_y
        
        self.isclicked = False
        
        self.render()
        
        
 
    def render(self):
        image_text = self.font.render(self.text, True, self.font_color, self.color_background)
        
        self.slave = pygame.surface.Surface((self.w,self.h))#superficie que se adapte a la del boton
        self.slave_rect = self.slave.get_rect()
        
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_x
        self.slave_rect_collide.y += self.master_y 
        
        
        self.slave.fill(self.color_background)
        
        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self.w / 2
        media_vertical = self.h / 2

        diferencia_horizontal = media_horizontal - media_texto_horizontal 
        diferencia_vertical = media_vertical - media_texto_vertical
        
        self.slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))
    
    def update(self, lista_eventos):
        self.isclicked = False
        for evento in lista_eventos:
           if evento.type == pygame.MOUSEBUTTONDOWN:
               if self.slave_rect_collide.collidepoint(evento.pos):
                   self.isclicked = True
                   self.onclick(self.onclick_param)
                   break
        self.draw()
                    
    def set_text(self, text):
        self.text = text
        self.render()

    def draw(self):
        self.master.blit(self.slave,self.slave_rect)
        pygame.draw.rect(self.master, self.color_border, self.slave_rect)

'''
class TextBox():
    def __init__(
            self, screen,master_x,master_y, x,y,w,h,
            color_background,color_background_seleccionado,color_border, color_border_seleccionado,font, font_size,
            font_color,border_size = -1):
        self.master = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.border_size = border_size
        
        pygame.font.init()#llamo al constructor de la fuente porque sino a veces pincha
        self.color_background_default = color_background
        self.color_border_default = color_border
        self.color_background_seleccionado = color_background_seleccionado
        self.color_border_seleccionado = color_border_seleccionado
        self.text = ""
        self.font = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.master_x = master_x
        self.master_y = master_y
        
        self.is_selected = False
        
        self.render()
        
    def get_text(self):
        return self._text    
    
    def set_text(self,texto):
        self.text = texto
        self.render()   
    
    def render(self):
        image_text = self.font.render(self.text, True, self.font_color, self.color_background)
        
        self.slave = pygame.surface.Surface((self.w,self.h))#superficie que se adapte a la del boton
        self.slave_rect = self.slave.get_rect()
        
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_x
        self.slave_rect_collide.y += self.master_y
        
        
        self.slave.fill(self.color_background)
        
        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self.w / 2
        media_vertical = self.h / 2
        diferencia_horizontal = media_horizontal - media_texto_horizontal 
        diferencia_vertical = media_vertical - media_texto_vertical
        
        self.slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))#podriamos sacar cuentas para centrar el texto, por el momento 10-10
        
    
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos):#me hicieron click, esto no siempre va a funcionar
                    self.color_background = self.color_background_seleccionado
                    self.color_border = self.color_border_seleccionado
                    self.is_selected = True
                else:
                    self.color_background = self.color_background_default
                    self.color_border = self.color_border_default
                    self.is_selected = False
                self.render()
            elif self.is_selected and evento.type == pygame.KEYDOWN:
                caracter = evento.unicode
                if evento.key == pygame.K_BACKSPACE:
                   self.text = self._text[:-1]
                #elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C':
                #    self._text += caracter
                self.render()
        self.draw()
    
    def draw(self):
        self.master.blit(self.slave,self.slave_rect)
        pygame.draw.rect(self.master, self.color_border, self.slave_rect, self.border_size)
'''   