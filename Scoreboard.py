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
        font=("Consolas", 12),
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
