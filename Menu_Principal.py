from tkinter import *
from Funciones_Basicas import *
from vlc import *

about = """

Sobre este juego:

Hecho en Costa Rica

Instituto Tecnológico de Costa Rica

Ingeniería en Computadores

Taller de Programación , primer año , grupo 2

Profesor Milton Villegas Lemus

Asistente José Morales

versión: 1.0

Autores: José Ignacio Castillo y Víctor Ortiz Cerón

Autor del módulo de Menú (Modificado por Víctor Ortiz): José Morales

Autores de los módulos de juego: Víctor Ortiz Cerón con Asistencia de Ramses Gutierrez

Autores del módulo Control_Pantallas: Víctor Ortiz Cerón con Asistencia de Ramses Gutierrez

"""
ventana = Tk()
ventana.title("Mars Under Fire")
ventana.minsize(600,800)
ventana.resizable(width = NO, height = NO)

fuente = fuente = ("8BIT WONDER",15)

C_menu = Canvas(ventana, width = 600 , height = 800)
C_menu.place(x = 0, y = 0)

C_menu.fondo = cargar_img('FONDOMENU.png')#Se establece la imagen de fondo del menu.
Fondo1 = C_menu.create_image(0,0,anchor = NW, image = C_menu.fondo)

C_menu.titulo = cargar_img('Titulo.png')#Se establece la imagen de fondo del menu.
Fondo1 = C_menu.create_image(5,10,anchor = NW, image = C_menu.titulo)

MenuMusic = True
reproductor = vlc.MediaPlayer()
cancion = cargarMP3('MenuSong.mp3')

def MenuLoop():
    global MenuMusic
    if MenuMusic:
        reproducir_cancion(cancion)
    ventana.after(61000,MenuLoop)
    
MenuLoop()


def abrir_about():
    detener_cancion()
    V_about = Toplevel()
    V_about.title("Sobre este Juego")
    V_about.minsize(1024,768)
    V_about.resizable(width = NO, height = NO)
    ventana.withdraw()
    C_about = Canvas(V_about, width = 1024 , height = 768)
    C_about.place(x = 0, y = 0)
    C_about.fondo = cargar_img('FONDOMENU2.png')
    Fondo3 = C_about.create_image(0,0,anchor = NW, image = C_about.fondo)
    C_about.tec = cargar_img('TecLogo.png')
    Logo = C_about.create_image(450,200,anchor = NW, image = C_about.tec)
    C_about.create_text(430,280, text = about, fill = "Black", font = ("arial",13) ) 
    C_about.pack()

    #Funcion que destruye la el toplevel V_about, para volver al menú. Inicia tambien la reproduccion de la musica de menú.
    def destroy_window():
        detener_cancion()
        cancion = cargarMP3('MenuSong.mp3')
        reproducir_fx(cancion)
        ventana.deiconify()
        V_about.destroy()
    V_about.protocol("WM_DELETE_WINDOW",destroy_window)

def abrir_scores():
    print("Scores")

def Empezar_Juego():
    print("Corre Juego")

def Empezar_Juego2():
    print("Corre Juego1")

def Empezar_Juego3():
    print("Corre Juego2")

Btn_Start = Button(ventana, text = 'Level 1',font = fuente, width = 20,command = Empezar_Juego)
Btn_Start.place(x = 110, y = 200)

Btn_Start2 = Button(ventana, text = 'Level 2',font = fuente, width = 20,command = Empezar_Juego2)
Btn_Start2.place(x = 110, y = 300)

Btn_Start2 = Button(ventana, text = 'Level 3',font = fuente, width = 20,command = Empezar_Juego3)
Btn_Start2.place(x = 110, y = 400)

Btn_about = Button(ventana, text = 'About this game',font = fuente, width = 20,command = abrir_about)
Btn_about.place(x = 110, y = 500)

Btn_Scores = Button(ventana, text = 'Scoreboard',font = fuente, width = 20,command = abrir_scores)
Btn_Scores.place(x = 110, y = 600)


ventana.mainloop()
