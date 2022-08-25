# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 07:03:31 2021

@author: Casa
"""
import turtle

def greeting():
    nombre = input("Buenos dias. Ingresa tu nombre:")
    print("Hola " + nombre + " Bienvenido a mi programa")
    adult(nombre)

def adult(name__):
    
    edad = 0
    while (edad < 18):
        edad = int(input("ingresa tu edad: "))
        
        if int(edad) < 18:
           print("no puedes pasar " + name__) 
        else:
            print("puedes pasar " + name__)
            dibujo()
        
def dibujo():
    window = turtle.Screen()
    dave =  turtle.Turtle()
    hacer_cuadro(dave)
    turtle.mainloop()
    
def hacer_cuadro(dave):
    length = int(input("tammaño del cuadrado"))
    
    for i in range(4):
        hacer_linea_y_girar(dave,length)
    print("cuadrado hecho.")
        
def hacer_linea_y_girar(dave, length):
    dave.forward(length)
    dave.left(90)
    
if __name__ == '__main__':
    greeting()
