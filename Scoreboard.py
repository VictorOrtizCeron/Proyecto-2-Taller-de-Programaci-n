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

from tkinter import *
from os import path
import vlc
from threading import Thread
from Funciones_Basicas import*
from Control_Pantallas import *
from Funciones_Scoreboard import *


def Score_Board():

    def Ir_a_Menu():
        Result.destroy()


    Result = Toplevel()
    Result.title("Resultados Partida")
    Result.minsize(600, 800)
    C_Scores = Canvas(Result, width = 600 , height = 800)
    Result.resizable(width=NO, height=NO)
    C_Scores.place(x = 0, y = 0)
    C_Scores.fondo = cargar_img('FONDOMENU.png')
    Fondo = C_Scores.create_image(0,0,anchor = NW, image = C_Scores.fondo)
    C_Scores.create_text(300,80, text = 'SCOREBOARD', fill = "Black", font = ("8BIT WONDER",25) )
    C_Scores.create_text(300,250, text = get_datas(0), fill = "Black", font = ("Arial",20) )
    C_Scores.pack()
    
    Result.protocol("WM_DELETE_WINDOW",Ir_a_Menu)

    Result.mainloop()