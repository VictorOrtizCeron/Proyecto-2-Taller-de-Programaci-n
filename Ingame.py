from tkinter import *
from Funciones_Basicas import *
from random import randint

Tiempo = 0
Score = 0
level = 1

def crear_ventana():
    global ventana
    ventana = Toplevel()
    ventana.geometry("1024x768")
    ventana.resizable(width = NO, height = NO)

def juego():



    fondo = Canvas(ventana,width = 1024, height = 768)
    ventana.fondo = cargar_img('FONDOMENU2.png')#Se establece la imagen de fondo del menu
    Fondo1 = fondo.create_image(0,0,anchor = NW, image = ventana.fondo)

    fondo.Tanque_img = cargar_img("Tanque/Tanque-1.png")
    Tanque = fondo.create_image(432,650, anchor = NW, image = fondo.Tanque_img)

    Temporizador = fondo.create_text(300,740, text = Tiempo, fill = "white", font = ("8BIT WONDER",13) )
    Scorer = fondo.create_text(500,740, text = Score, fill = "white", font = ("8BIT WONDER",13) )
    lvl = fondo.create_text(680,740, text = level, fill = "white", font = ("8BIT WONDER",13) )
    name_Temp = fondo.create_text(200,740, text = 'Timer:', fill = "white", font = ("8BIT WONDER",13) )
    name_Score = fondo.create_text(400,740, text = 'Score:', fill = "white", font = ("8BIT WONDER",13) )
    name_lvl = fondo.create_text(600,740, text = 'Level:', fill = "white", font = ("8BIT WONDER",13) )
    



    fondo.pack()
    