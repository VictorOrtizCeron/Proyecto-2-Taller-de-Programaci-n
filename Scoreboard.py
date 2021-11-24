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
    def Ir_a_Menu():
        Result.destroy()

    Result = Toplevel()
    Result.title("Altos puntajes")
    Result.minsize(375, 420)
    Result.resizable(width=NO, height=NO)
    L_about = Label(
        Result,
        text=get_datas(Scr),
        font=("8BIT WONDER",12),
    )



    Result.mainloop()
