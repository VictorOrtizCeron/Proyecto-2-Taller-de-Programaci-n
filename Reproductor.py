from tkinter import *
import vlc
from os import path


def cargarMP3(nombre):
    return path.join("AssetsGame", nombre)


def reproducir_fx(archivoMP3):
    vlc.MediaPlayer(archivoMP3).play()


def detener_cancion():
    global reproductor
    if isinstance(reproductor, vlc.MediaPlayer):
        reproductor.stop()


def reproducir_cancion(archivoMP3):
    global reproductor
    detener_cancion()
    reproductor = vlc.MediaPlayer(archivoMP3)
    reproductor.audio_set_volume(50)
    reproductor.play()


def Cancion_Menu():
    cancion = cargarMP3("InsertSongName.lol")
    reproducir_cancion(cancion)


def CancionJuego():
    cancion = cargarMP3("InsertSongName.lol")
    reproducir_cancion(cancion)