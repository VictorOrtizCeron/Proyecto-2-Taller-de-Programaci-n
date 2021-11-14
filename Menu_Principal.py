from tkinter import *
from Funciones_Basicas import *

about = """

Sobre este juego:

Hecho en Costa Rica

Instituto Tecnológico de Costa Rica

Ingeniería en Computadores

Taller de Programación , primer año , grupo 2

Profesor Milton Villegas Lemus

Asistente José Morales

versión: 1.0

Autores: José Ignacio Castillo y Víctor Ortiz Cerón

Autor del módulo de Menú (Modificado por Víctor Ortiz): José Morales

Autores de los módulos de juego: Víctor Ortiz Cerón con Asistencia de Ramses Gutierrez

Autores del módulo Control_Pantallas: Víctor Ortiz Cerón con Asistencia de Ramses Gutierrez

"""
ventana = Tk()
ventana.title("Deep Trouble")
ventana.minsize(600,800)
ventana.resizable(width = NO, height = NO)

fuente = fuente = ("8BIT WONDER",15)

C_menu = Canvas(ventana, width = 600 , height = 800)
C_menu.place(x = 0, y = 0)

C_menu.fondo = cargar_img('FONDOMENU.png')#Se establece la imagen de fondo del menu.
Fondo1 = C_menu.create_image(0,0,anchor = NW, image = C_menu.fondo)

ventana.mainloop()
