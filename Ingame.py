
"""
 Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores

    Lenguaje: Python 3.9.6
    Autores:  Victor Ortiz Ceron(vortiz@estudiantec.cr) , José Ignacio Castillo()
    Tutor: Ramses Gutiérrez
    Versión: 1.0
    Fecha última Modificación: ---
    Módulo: Ingame.Py
    Descripción del módulo: Este es un módulo auxiliar que contiene todas la funciones y actividades de juegos, si se escoge el level 1. Este código
    fue creado en parte utilizando como referencia primordial las tutorias del tutor Ramses Gutiérrez. Sin embargo, el código visto fue modificado para acomodar
    las necesidades del juego por Víctor Ortiz y José Ignacio Castillo.
"""

#Importación de los módulos y bibliotecas necesarias
from tkinter import *
from Funciones_Basicas import *
from random import randint
from threading import *
from Funciones_Scoreboard import *

#Definición de variables globales
Tiempo = 0 #Tiempo Transcurrido
Score = 0 #Puntaje obtenido
level = 1 #Nivel actual
direc = [False,False,False,False] #Direcciones de movimiento
Running = True # Condición para correr el juego, o detenerlo
pause = False # Condición para pausar el juego
GameOver = False #Condición de finalización del juego
Quit = False #Función que cierra el juego, sin scores
GeneratorSpeed = 2000 #Tiempo entre la generación de misiles enemigos
salto = True #Condición para configurar salto
Speed = 45 #Velocidad de movimiento de los misiles disparados
MisilCoords = [0,0] #Coordenadas de los misiles disparados
MisilEnemigoCoords = [0,0] #Coordenadas de los misiles enemigos
Life = 3 #Cantidad de vidas restantes
name = '' #Nombre del jugador
GameOver = False #Condición de pantalla de perdida
vel = 10 #Velocidad de movimiento de los misiles enemigos

def crear_ventana():#Crea la ventana principal de juego
    global ventana
    ventana = Toplevel()
    ventana.geometry("1024x768")
    ventana.resizable(width = NO, height = NO)

def juego():#Función principal de juego

    def Restart():#Función que reinicia todas las variables globales a sus datos originales
        global direc,Running,GameOver,ventana,pause, Tiempo,Score,Quit,level,GeneratorSpeed,Speed,name,Life,vel
        direc = [False,False,False,False]
        Running = True
        GameOver = False
        pause = False
        Tiempo = 0
        Score= 0
        Quit = False
        level = 1
        Speed = 45
        GeneratorSpeed = 1000
        Life = 3
        name = ''
        vel = 10
    Restart()

    def Game_Over(): #Función de perdida de juego
        global GameOver , Score , Quit
        gameover = cargarMP3('GameOver.mp3')
        if GameOver == True and Quit == False:

            #Crea el texto 'Game Over' y reproduce el audio denotado GameOver.mp3
            fondo.create_text(520,300, text = 'GAME OVER ', fill = "black", font = ("8BIT WONDER",40) )
            fondo.create_text(520,350, text = ('Score:',Score), fill = "black", font = ("8BIT WONDER",25) )
            reproducir_fx(gameover)

            #Crea la barra de entrada para capturar el nombre del usuario.
            E_nombre = Entry(ventana, width = 10, font = ('8BIT WONDER',20) )
            E_nombre.place(x = 370 ,y = 420)

            #Función que genera un texto que confirma la captura del nombre del usuario.
            def get_Name():
                global Nombre
                Nombre = E_nombre.get()
                print(Nombre)
                print(Score)
                fondo.create_text(520,550, text = ('Score Saved'), fill = "black", font = ("8BIT WONDER",20) )
                save_data(Nombre,Score)

            #Crea el botón para capturar el nombre.
            Btn_enter = Button(ventana, text = 'Enter',font = ('8BIT WONDER',20), width = 7,command = get_Name)
            Btn_enter.place(x = 410, y = 460)
    


    
    #Se define el canvas de la pantalla
    fondo = Canvas(ventana,width = 1024, height = 768)

    ventana.fondo = cargar_img('FONDOMENU2.png')#Se establece la imagen de fondo del menu
    Fondo1 = fondo.create_image(0,0,anchor = NW, image = ventana.fondo)

    #Se establecen todos los elementos visuales de la pantalla de juego
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
    Vidas = fondo.create_text(700,740, text = "Lives:", fill = "white", font = ("8BIT WONDER",13) )
    st = fondo.create_text(520,350, text = 'Press P to Start', fill = "black", font = ("8BIT WONDER",30) )
    fondo.heart1 = cargar_img("Heart.png")
    fondo.heart2 = cargar_img("Heart.png")
    fondo.heart3 = cargar_img("Heart.png")
    Life1 = fondo.create_image(760,720, anchor = NW, image = fondo.heart1)
    Life2 = fondo.create_image(820,720, anchor = NW, image = fondo.heart2)
    Life3 = fondo.create_image(880,720, anchor = NW, image = fondo.heart3)
    fondo.pack()

    #Función que determina la dirección de movimiento del tanque utilizando la lista de booleanos direc, 
    # dependiendo de la presión de teclas.
    def teclaIn(event):
        global direc, Running , pause
        if Running:
            if event.keysym == 'Up': #El tanque se propulsa para arriba hasta un limite de altura y luego cae.
                direc[3] = True
                salto_aux()
            if event.keysym == 'Down':#El tanque se mueve para abajo.
                direc[2] = True
            if event.keysym == 'Left':#El tanque se mueve para izquierda.
                direc[1] = True
            if event.keysym == 'Right':#El tanque se mueve para derecha.
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
            if event.keysym == 'x':#Activa la función de disparo del misil, para evitar el efecto laser
                generar_misil()
            
    
    def volar():#Configura el sprite del tanque mientras está en el aire
        global direc , salto
        coordenadas = fondo.coords(Tanque)
        if direc[3]== True and salto == True:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img2 )
        else:
            fondo.itemconfig(Tanque,image = fondo.Tanque_img )
        ventana.after(5,volar)
    volar()

    def mover():# Función que mueve el tanque dependiendo de las teclas presionadas
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

            ventana.after(10,mover)  
    mover()
    
    def salto_aux():#Función que determina las limitaciones del salto del tanque como la altura, y la habilidad para saltar 2 veces
        global salto
        coordenadas = fondo.coords(Tanque)
        if coordenadas[1] > 630:
            salto = True
        else:
            salto = False
        
        

    def MovingDown():# función que define la velocidad de caida del tanque
        
        if Running and fondo.coords(Tanque)[1] + 84 < 730:
            if pause:
                fondo.move(Tanque,0,5)
        ventana.after(5,MovingDown)

    MovingDown()        
    mover()

    #Creación de eventos, y definición de funciones para llevar a cabo.
    ventana.bind('<KeyPress>', teclaIn)
    ventana.bind('<KeyRelease>',teclaOut)
    

    def temporizador(): #Función que configura el temporizador,el nivel y la dificultad dependiendo del tiempo transcurrido
        global Tiempo , Score , level , vel
        if Running:
            if pause:
                if level == 1:
                    #Condición de  nivel 1 , asi como incrementos de dificultad 
                    #Sube nivel
                    if Tiempo % 40 == 0 and Tiempo != 0:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        level = level + 1
                        fondo.itemconfig(lvl,text = level)
                    else:
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                        

                if level == 2:
                    #Condición de  nivel 2 , asi como incrementos de dificultad.
                    vel = 15
                    #Sube nivel
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
                        vel = 20
                        Tiempo = Tiempo + 1
                        fondo.itemconfig(Temporizador, text = Tiempo)
                                      
            ventana.after(1000,temporizador)
    temporizador()


    
    def check_lives(Life1, Life2, Life3):#Función que borra las imagenes de los corazones en caso de colisión, y activa el game over 
        global Life, Running, GameOver
        if Running:
            if pause:
                if Life == 2:
                    fondo.delete(Life1)
                elif Life == 1:
                    fondo.delete(Life2)
                else:
                    if Life == 0:
                        fondo.delete(Life3)
                        GameOver = True
                        Running = False
                        Game_Over()
            ventana.after(10, lambda : check_lives(Life1, Life2, Life3))
    
    check_lives(Life1, Life2, Life3)            
            
    def generar_misil():#Función que genera un misil cuando se presion x
        if Running:
            if pause:
                global MisilEnemigoCoords,MisilCoords
                coordenadas = fondo.coords(Tanque)
                x = coordenadas[0]
                y = coordenadas[1]
                misil = fondo.create_image(x+25,y-20,anchor = NW , image= fondo.Misil)
                mover_misil(misil)
                

    def mover_misil(misil):#Función que mueve el misil creado en generar_misil()
        global MisilEnemigoCoords, MisilCoords
        if fondo.type(misil) and Running:
            if pause:
                coordenadas = fondo.coords(misil)
                if (coordenadas[1]+ 34)  <= 0 :
                    fondo.delete(misil)
                if coordenadas[1]< MisilEnemigoCoords[1]+60 and\
                    coordenadas[0]+12 > MisilEnemigoCoords[0]+5 and\
                    coordenadas[0]+24 < MisilEnemigoCoords[0]+60:#Condición de colisión con misil enemigo
                    fondo.delete(misil)  
                else:
                    fondo.move(misil,0,-1)

                MisilCoords = coordenadas   
            ventana.after(5, lambda : mover_misil(misil))


    def mover_misil_Enemigo(obstaculo):# Mueve los misiles enemigos generados en Generar_MisilEnemigo_Aux
        global Running ,Speed, MisilEnemigoCoords, MisilCoords, Score
        if fondo.type(obstaculo) and Running:
            if pause:
                MisilEnemigoCoords = fondo.coords(obstaculo)
                
                if MisilEnemigoCoords[1]+ 64 >= 730:
                    fondo.delete(obstaculo)
                if  MisilCoords[1]< MisilEnemigoCoords[1]+60 and\
                    MisilCoords[0]+12 > MisilEnemigoCoords[0]+5 and\
                    MisilCoords[0]+24 < MisilEnemigoCoords[0]+60: #Condición de colisión entre misiles
                    fondo.delete(obstaculo)
                    Score = Score + 2
                    fondo.itemconfig(Scorer, text = Score)



                    
                else:
                    fondo.move(obstaculo,0,vel)
                                    
            ventana.after(50,lambda: mover_misil_Enemigo(obstaculo))


    def generar_MisilEnemigo_aux():#Genera misiles enemigos de forma constante
        global Running , GeneratorSpeed
        if Running:
            if pause:
                x= randint(100,850)
                misilEnemigo = fondo.create_image(x,0, anchor = NW, image = fondo.MisilEnemigo)
                mover_misil_Enemigo(misilEnemigo)
                colision_misil_aux(misilEnemigo)
                    
                    
            ventana.after(GeneratorSpeed ,lambda: generar_MisilEnemigo_aux())

    generar_MisilEnemigo_aux()
    
    
    def colision_misil_aux(misil):
        global Running , GameOver , Life,vel
            #Condicional de delimitación de lista de coordenadas cuando el obstáculo sale de la pantalla de juego.
        if fondo.type(misil) and Running:
            if pause:
                coordenadas_Tanque = fondo.coords(Tanque)
                coordenadas_misil = fondo.coords(misil)
                if (coordenadas_misil[0]+16) < (coordenadas_Tanque[0]+75) and \
                    (coordenadas_misil[0]+ 48)>(coordenadas_Tanque[0]+16) and \
                    (coordenadas_misil[1]+12) < (coordenadas_Tanque[1]+64) and \
                    (coordenadas_misil[1] + 60 ) > (coordenadas_Tanque[1]+20):#Condición de colisión de misil enemigo con el tanque
                    fondo.delete(misil)
                    Life = Life - 1        
        ventana.after(vel,lambda : colision_misil_aux(misil))

    def stop():#Función para finalizar la ventana sin protocolo de game over
        global Running , Quit
        Quit = True
        Running = False

    ventana.protocol("WM.DELETE_WINDOW", stop)
    
    