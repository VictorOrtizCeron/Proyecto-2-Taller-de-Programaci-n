from tkinter import *

def destroy_window():
        #   Retorna al menu
        
        V_about.destroy()

V_about = Toplevel()
V_about.title("Informacion del juego")
V_about.minsize(300, 420)
V_about.resizable(width=NO, height=NO)

    #   Texto about
L_about = Label(
        V_about,
        text="""
    País:
    Costa Rica

    Universidad y carrera:
    Instituto Tecnológico de Costa Rica
    Ingenieria de computadores

    Taller de programación, grupo 2
    Semestre II

    Profesor:
    Milton Villegas Lemus

    Versión del programa:
    1.0

    Autores:
    Victor Ortiz Ceron
    Ignacio Castillo Montero
    """,
        bg="black",
        fg="white",
    )
L_about.place(x=50, y=0)

Back = Button(
        V_about,
        text="Menu Principal",
        bg="black",
        fg="white",
        font="Arial",
        command=destroy_window,
    )
Back.place(x=110, y=360)

V_about.mainloop()
    