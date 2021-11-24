"""
 Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores

    Lenguaje: Python 3.9.6
    Autor:  Victor Ortiz Ceron(vortiz@estudiantec.cr) 
    Tutor: Ramses Gutiérrez
    Versión: 1.0
    Fecha última Modificación: 22/10/2021
    Módulo: Control_Pantallas.py
    Descripción del módulo: Este es un módulo auxiliar hecho con la tutoría de Ramses Gutiérrez, con el fin de manejar las ventanas del juego
    de forma no local en las diferentes etapas de su ejecución.  
"""

#Importación de las bibliotecas necesarias para el funcionamiento de las funciones.
from tkinter import *
import Ingame

#import Ingame2
#import Ingame3

#Variable maun utilizada para referirse a la ventana del menu principal una vez abierto el juego en los distintos niveles.
main = None


#Función que abre la ventana de juego y esconde el menú cuando se escoge el nivel 1.
def abrir_juego(Main):
    global main , close
    main = Main
    main.withdraw()
    Ingame.crear_ventana()
    Ingame.juego()
    Ingame.ventana.protocol("WM_DELETE_WINDOW",cerrar_juego)

#Función que abre la ventana de juego y esconde el menú cuando se escoge el nivel 2.
"""
def abrir_juego2(Main):
    global main , close
    main = Main
    main.withdraw()
    Ingame2.crear_ventana()
    Ingame2.juego()
    Ingame2.ventana.protocol("WM_DELETE_WINDOW",cerrar_juego2)

#Función que abre la ventana de juego y esconde el menú cuando se escoge el nivel 3.
def abrir_juego3(Main):
    global main , close
    main = Main
    main.withdraw()
    Ingame3.crear_ventana()
    Ingame3.juego()
    Ingame3.ventana.protocol("WM_DELETE_WINDOW",cerrar_juego3)
"""       
#Función que cierra la venta de juego, abre la del menú y destruye la de juego cuando se escoge el nivel 1.
def cerrar_juego():
    main.deiconify()
    Ingame.ventana.destroy()

#Función que cierra la venta de juego, abre la del menú y destruye la de juego cuando se escoge el nivel 2.   
"""
def cerrar_juego2():
    main.deiconify()
    Ingame2.ventana.destroy()

#Función que cierra la venta de juego, abre la del menú y destruye la de juego cuando se escoge el nivel 3.
def cerrar_juego3():
    main.deiconify()
    Ingame3.ventana.destroy()
    """