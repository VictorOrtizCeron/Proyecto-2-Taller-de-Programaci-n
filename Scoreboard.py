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
#from Funciones_Scoreboard import *
from Funciones_Basicas import*
from Control_Pantallas import *
from Funciones_Scoreboard import *
from Ingame import Score as Scr

def Score_Board():
    #funcion la cual crea una ventana con la scoreboard
    def Ir_a_Menu():
        Result.destroy()

    Result = Toplevel()
    Result.title("Altos puntajes")
    Result.minsize(375, 420)
    Result.resizable(width=NO, height=NO)
    #Configuracion de la ventana
    L_about = Label(
        Result,
        text=get_datas(Scr),
        font=("8BIT WONDER",15),
        #aca se llama a get_datas de funciones_scoreboard.py para la informacion de scores.txt y se le da formato
    )



    Result.mainloop()
