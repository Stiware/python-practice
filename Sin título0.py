# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:25:03 2021

@author: Casa
"""

import csv
import matplotlib.pyplot as plt
import numpy as np


result = []
Age = []

with open('theatre.csv') as file:
    #reader = csv.DictReader(file)
    lineas = file.read().splitlines();
    lineas.pop(0);
    for i in lineas:
        linea = i.split(',')
        Age.append(float(linea[2]))


#Definir los datos
x1 = Age
y1 = [10, 55, 90, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]
#Configurar las características del gráfico
plt.bar(x1, y1, label = 'Datos 1', width = 0.5, color = 'lightblue')
plt.bar(x2, y2, label = 'Datos 2', width = 0.5, color = 'orange')
#Definir título y nombres de ejes
plt.title('Gráfico de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()
