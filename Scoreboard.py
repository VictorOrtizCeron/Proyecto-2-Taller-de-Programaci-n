"""
 Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores

    Lenguaje: Python 3.9.6
    Autores:  Victor Ortiz Ceron(vortiz@estudiantec.cr) , José Ignacio Castillo()
    Tutor: Ramses Gutiérrez
    Versión: 1.0
    Fecha última Modificación: 24/11/2021
    Módulo: Funciones_Scoreboard.py
    Descripción del módulo: Este modulo es el scoreboard en si, el cual gracias a Funciones_Scoreboard 
    Entradas: Informacion de 'get_datas' de funciones_scoreboard.py
    Salidas: display de la scoreboard
"""
#Importaciones de módulos y bibliotecas necesarias
from tkinter import *
from os import path
import vlc
from threading import Thread
from Funciones_Basicas import*
from Control_Pantallas import *
from Funciones_Scoreboard import *


def Score_Board():#creacion de la ventana del scoreboard

    def Ir_a_Menu():#Función para cerrar la ventana de puntajes
        Result.destroy()


    Result = Toplevel()#creacion de la ventana de puntajes
    Result.title("Resultados Partida")#nombre de la ventana 
    Result.minsize(600, 800)#tamaño de la ventana
    C_Scores = Canvas(Result, width = 600 , height = 800)#creacion del canvas
    Result.resizable(width=NO, height=NO)#no se puede cambiar el tamaño de la ventana
    C_Scores.place(x = 0, y = 0)#posicion del canvas
    C_Scores.fondo = cargar_img('FONDOMENU.png')#carga la imagen de fondo
    Fondo = C_Scores.create_image(0,0,anchor = NW, image = C_Scores.fondo)#creacion de la imagen de fondo
    C_Scores.create_text(300,80, text = 'SCOREBOARD', fill = "Black", font = ("8BIT WONDER",25) )#creacion del encabezado de la ventana
    C_Scores.create_text(300,400, text = get_datas(0), fill = "Black", font = ("Arial",20) )#creación del texto de los puntajes
    C_Scores.pack()#pack para que se vea la ventana
    
    Result.protocol("WM_DELETE_WINDOW",Ir_a_Menu)#función que se ejecuta al cerrar la ventana

    Result.mainloop()#loop para que se vea la ventana