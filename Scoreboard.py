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
from Ingame import Score as Scr

def Score_Board():
    def Ir_a_Menu():
        Result.destroy()
    Result = Toplevel()
    Result.title("Resultados Partida")
    Result.minsize(420, 530)
    Result.resizable(width=NO, height=NO)
    L_about = Label(
        Result,
        text=get_datas(0),
        font=("Consolas", 10),
    )

    Back = Button(
        Result,
        text="Menu Principal",
        bg="black",
        fg="white",
        font="Arial",
        command=Ir_a_Menu,
    )
    L_about.place(x=50, y=50)
    Back.place(x=110, y=360)

    Result.mainloop()