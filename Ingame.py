from tkinter import *
from Funciones_Basicas import *
from random import randint
from threading import *


Tiempo = 0
Score = 0
level = 1
direc = [False,False,False,False] 
Running = True
pause = False
Nombre = "Unknown"
GameOver = False
Quit = False
GeneratorSpeed = 1000
salto = True
Speed = 45

def crear_ventana():
    global ventana
    ventana = Toplevel()
    ventana.geometry("1024x768")
    ventana.resizable(width = NO, height = NO)

def juego():

    def Restart():
        global direc,Running,GameOver,ventana,pause, Tiempo,Score,Quit,Nombre,level,GeneratorSpeed,Speed
        direc = [False,False,False,False]
        Running = True
        GameOver = False
        pause = False
        Tiempo = 35
        Score= 0
        Quit = False
        Nombre = 'Unknown'
        level = 1
        Speed = 45
        GeneratorSpeed = 1000
    


    global direc,Running

    fondo = Canvas(ventana,width = 1024, height = 768)
    ventana.fondo = cargar_img('FONDOMENU2.png')#Se establece la imagen de fondo del menu
    Fondo1 = fondo.create_image(0,0,anchor = NW, image = ventana.fondo)

    fondo.Tanque_img = cargar_img("Tanque/Tanque-1.png")
    fondo.Tanque_img2 = cargar_img("Tanque/Tanque-2.png")
    fondo.Misil = cargar_img("Misil.png")
    fondo.MisilEnemigo = cargar_img("MisilEnemigo.png")
    Tanque = fondo.create_image(432,650, anchor = NW, image = fondo.Tanque_img)
    

    

    Temporizador = fondo.create_text(200,740, text = Tiempo, fill = "white", font = ("8BIT WONDER",13) )
    Scorer = fondo.create_text(400,740, text = Score, fill = "white", font = ("8BIT WONDER",13) )
    lvl = fondo.create_text(580,740, text = level, fill = "white", font = ("8BIT WONDER",13) )
    name_Temp = fondo.create_text(100,740, text = 'Timer:', fill = "white", font = ("8BIT WONDER",13) )
    name_Score = fondo.create_text(300,740, text = 'Score:', fill = "white", font = ("8BIT WONDER",13) )
    name_lvl = fondo.create_text(500,740, text = 'Level:', fill = "white", font = ("8BIT WONDER",13) )
    
    st = fondo.create_text(520,350, text = 'Press P to Start', fill = "black", font = ("8BIT WONDER",30) )

    fondo.pack()
    #Función que determina la dirección de movimiento del submarino utilizando la lista de booleanos direc, 
    # dependiendo de la presión de teclas.
    def teclaIn(event):
        global direc, Running , pause
        if Running:
            if event.keysym == 'Up': #El submarino se mueve para arriba.
                direc[3] = True
                salto_aux()
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
        global direc,Running,salto
        if Running:
            if event.keysym == 'Up':
                direc[3] = False
            if event.keysym == 'Down':
                direc[2] = False
            if event.keysym == 'Left':
                direc[1] = False
            if event.keysym == 'Right':
                direc[0] = False
            if event.keysym == 'x':
                disparo()
    
    def volar():
        global direc , salto
        coordenadas = fondo.coords(Tanque)
        if direc[3]== True and salto == True:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img2 )
        else:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img )
        ventana.after(5,volar)
    volar()


    
    def disparo():
        if Running:
            if pause:
                generar_misil()
                
    def generar_misil():
        coordenadas = fondo.coords(Tanque)
        x = coordenadas[0]
        y = coordenadas[1]
        misil = fondo.create_image(x+25,y-20,anchor = NW , image= fondo.Misil)
        mover_misil(misil)
    
    def mover_misil(misil):
        if fondo.type(misil) and Running:
            if pause:
                coordenadas = fondo.coords(misil)
                if coordenadas[1]+ 34  <= 0:
                    fondo.delete(misil)
                else:
                    fondo.move(misil,0,-8)
            ventana.after(30,lambda: mover_misil(misil))


    def mover():
        global direc,salto
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
                if direc[3] and coordenadas[1] > 300 and salto == True:
                        fondo.move(Tanque, 0,-8)

            ventana.after(5,mover)  
    
    def salto_aux():
        global salto
        coordenadas = fondo.coords(Tanque)
        if coordenadas[1] > 630:
            salto = True
        else:
            salto = False
        
        

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


    

    def mover_obstaculo(obstaculo):
        global Running ,Speed
        if fondo.type(obstaculo) and Running:
            if pause:
                coordenadas = fondo.coords(obstaculo)
                if coordenadas[1]+ 64 >= 730:
                    fondo.delete(obstaculo)
                else:
                    fondo.move(obstaculo,0,10)
            ventana.after(Speed,lambda: mover_obstaculo(obstaculo))

    

    #Función que genera  los obstáculos , y luego los borra los obstáculos cuando sale de la pantalla de juego.
    def generar_MisilEnemigo_aux():
        global Running , GeneratorSpeed
        if Running:
            if pause:
                x= randint(0,950)
                misil = fondo.create_image(x,0, anchor = NW, image = fondo.MisilEnemigo)    
                mover_obstaculo(misil)
                colision_misil_aux(misil)
                
            ventana.after(GeneratorSpeed,generar_MisilEnemigo_aux)

    generar_MisilEnemigo_aux()
    
    def colision_misil_aux(misil):
        global Running , GameOver 
        #Condicional de delimitación de lista de coordenadas cuando el obstáculo sale de la pantalla de juego.
        if fondo.type(misil) and Running:
            if pause:
                coordenadas_Tanque = fondo.coords(Tanque)
                coordenadas_misil = fondo.coords(misil)
                if (coordenadas_misil[0]+16) < (coordenadas_Tanque[0]+75) and \
                    (coordenadas_misil[0]+ 48)>(coordenadas_Tanque[0]+16) and \
                    (coordenadas_misil[1]+12) < (coordenadas_Tanque[1]+64) and \
                    (coordenadas_misil[1] + 60 ) > (coordenadas_Tanque[1]+20):
                    #Valores iniciales para iniciar perdida de juego
                    #Running = False
                    #GameOver = True
                    print('Colisión')
                    
            ventana.after(1,lambda : colision_misil_aux(misil))
       