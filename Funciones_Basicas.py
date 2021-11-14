"""
 Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores

    Lenguaje: Python 3.9.6
    Autores:  Victor Ortiz Ceron y Jose Ignacio Castillo 
    Co-Autor: Jose Fernando Morales Vargas
    Versión: 1.0
    Fecha última Modificación: 22/10/2021
    Módulo: Funciones_Básicas
    Descripción del módulo: Este es un módulo auxiliar que contiene funciones básicas que pueden ser utilizadas en cualquier etapa del programa,
    por lo que es mejor mantenerlas aparte e importarlas cuando sea necesario utilizarlas. Dichas funciones en lus totalidad fueron creadas por
    el asistente Jose Fernando Morales Vargas durante las sesiones de Taller de programación, y posteriormente modificadas por Víctor Ortiz para 
    acomodar las necesidades del programa.
"""
#Importación de las bibliotecas necesarias para el funcionamiento de las funciones. 
from tkinter import *
from os import path
from random import randint
import vlc

#Inicia el media player de vlc.
reproductor = vlc.MediaPlayer()

#Es una funcion que encuentra una imagen utilizando su dirección relativa en el directorio, y la retorna.
def cargar_img(nombre):
    ruta  = path.join('Assets/', nombre)
    img=PhotoImage(file=ruta)
    return img

#Función que encuentra un mp3 utilizando su dirección relativa.
def cargarMP3(nombre):
    return path.join('elementos',nombre)

#Funcion que detiene la reproducción de un mp3
def detener_cancion():
    global reproductor
    if (isinstance(reproductor,vlc.MediaPlayer)):
        reproductor.stop()

#Funcion que reproduce un mp3 y detiene el anterior, si había otro sonando.         
def reproducir_cancion(archivoMP3):
    global reproductor
    detener_cancion()
    reproductor = vlc.MediaPlayer(archivoMP3)
    reproductor.audio_set_volume(50)
    reproductor.play()

#Función que hace lo mismo que reproducir_cancion pero delimitado para sonidos cortos y efectos.
def reproducir_fx(archivoMP3):
    global reproductor
    detener_cancion()
    reproductor = vlc.MediaPlayer(archivoMP3)
    reproductor.audio_set_volume(50)
    reproductor.play()