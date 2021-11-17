from tkinter import *
from Funciones_Basicas import *
from random import randint
import threading


Tiempo = 0
Score = 0
level = 1
direc = [False,False,False,False] 
Running = True
pause = False
Nombre = "Unknown"
GameOver = False
Quit = False
GeneratorSpeed = 5000

def crear_ventana():
    global ventana
    ventana = Toplevel()
    ventana.geometry("1024x768")
    ventana.resizable(width = NO, height = NO)

def juego():

    def Restart():
        global direc,Running,GameOver,ventana,pause, Tiempo,Score,Quit,Nombre,level,GeneratorSpeed
        direc = [False,False,False,False]
        Running = True
        GameOver = False
        pause = False
        Tiempo = 35
        Score= 0
        Quit = False
        Nombre = 'Unknown'
        level = 1
        GeneratorSpeed = 5000
    Restart()


    global direc,Running

    fondo = Canvas(ventana,width = 1024, height = 768)
    ventana.fondo = cargar_img('FONDOMENU2.png')#Se establece la imagen de fondo del menu
    Fondo1 = fondo.create_image(0,0,anchor = NW, image = ventana.fondo)

    fondo.Tanque_img = cargar_img("Tanque/Tanque-1.png")
    fondo.Tanque_img2 = cargar_img("Tanque/Tanque-2.png")
    Tanque = fondo.create_image(432,650, anchor = NW, image = fondo.Tanque_img)
    

    

    Temporizador = fondo.create_text(200,740, text = Tiempo, fill = "white", font = ("8BIT WONDER",13) )
    Scorer = fondo.create_text(400,740, text = Score, fill = "white", font = ("8BIT WONDER",13) )
    lvl = fondo.create_text(580,740, text = level, fill = "white", font = ("8BIT WONDER",13) )
    name_Temp = fondo.create_text(100,740, text = 'Timer:', fill = "white", font = ("8BIT WONDER",13) )
    name_Score = fondo.create_text(300,740, text = 'Score:', fill = "white", font = ("8BIT WONDER",13) )
    name_lvl = fondo.create_text(500,740, text = 'Level:', fill = "white", font = ("8BIT WONDER",13) )
    
    st = fondo.create_text(520,350, text = 'Press P to Start', fill = "black", font = ("8BIT WONDER",30) )

    #Función que determina la dirección de movimiento del submarino utilizando la lista de booleanos direc, 
    # dependiendo de la presión de teclas.
    def teclaIn(event):
        global direc, Running , pause
        if Running:
            if event.keysym == 'Up': #El submarino se mueve para arriba.
                direc[3] = True
            if event.keysym == 'Down':#El submarino se mueve para abajo.
                direc[2] = True
            if event.keysym == 'Left':#El submarino se mueve para izquierda.
                direc[1] = True
            if event.keysym == 'Right':#El submarino se mueve para derecha.
                direc[0] = True
            if event.keysym == 'p':#el juego se pausa. Si es la primera vez, borra el texto de 'Press P to start'.
                fondo.delete(st)
                #Condicional para pausar o resumir juego utilizando P.
                if pause: 
                    pause = False
                else:
                    pause = True

    #Función que detiene el movimiento del submarino al soltar las teclas presionadas. 
    def teclaOut(event):
        global direc,Running
        if Running:
            if event.keysym == 'Up':
                direc[3] = False
            if event.keysym == 'Down':
                direc[2] = False
            if event.keysym == 'Left':
                direc[1] = False
            if event.keysym == 'Right':
                direc[0] = False
    
    def volar():
        global direc 
        coordenadas = fondo.coords(Tanque)
        if direc[3]== True:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img2 )
        else:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img )

        

        ventana.after(5,volar)
    volar()

    def mover():
        global direc
        if Running:
            if pause:
                vel = 3
                coordenadas = fondo.coords(Tanque)
                if direc[0] and coordenadas[0] < 890:
                    fondo.move(Tanque, vel,0)
                if direc[2] and coordenadas[1]+ 84 < 730:
                    fondo.move(Tanque, 0,vel)
                if direc[1] and coordenadas[0] > 35:
                    fondo.move(Tanque, -vel,0)
                if direc[3] and coordenadas[1] > 20:
                    fondo.move(Tanque, 0,-8)
            ventana.after(5,mover)  
    
    def MovingDown():
        global VelY
        if Running and fondo.coords(Tanque)[1] + 84 < 730:
            if pause:
                fondo.move(Tanque,0,5)
        ventana.after(5,MovingDown)

    MovingDown()        
    mover()

    #Creación de eventos, y definición de funciones para llevar a cabo.
    ventana.bind('<KeyPress>', teclaIn)
    ventana.bind('<KeyRelease>',teclaOut)
    
    def temporizador():
        global Tiempo , Score , level , GeneratorSpeed
        if Running:
            if pause:
                if level == 1:
                    #Condición de  nivel 1 , asi como incrementos de dificultad y bonos.
                    #Bono y sube nivel
                    if Tiempo % 40 == 0 and Tiempo != 0:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        level = level + 1
                        fondo.itemconfig(lvl,text = level)
                    else:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        

                if level == 2:
                    #Condición de  nivel 2 , asi como incrementos de dificultad y bonos.
                    GeneratorSpeed = 4000
                    #Bono y sube nivel
                    if Tiempo % 80 == 0 and Tiempo != 0:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        level = level + 1
                        fondo.itemconfig(lvl,text = level)
                    else:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        

                if level == 3:
                        #Condición de  nivel 3 , ya no hay más bonos o niveles. 
                        GeneratorSpeed = 3000
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        
               
            ventana.after(1000,temporizador)
    temporizador()


    fondo.pack()
    