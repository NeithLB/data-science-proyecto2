# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:14:23 2020

@author: NEITH
"""
#Proyecto 2: Synergy logistics

#Exportar libreria CSV y llamar el archivo correspondiente en formato reader
import csv

lista_datos = []

with open ("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader (archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)
        
#print(lista_datos[0])

#Generar el menú de opciones diponibles 

#GENERAR RUTAS DE EXPORTACIÓN, usando un bucle for.

print ("Bienvedidos a Synergy logistics ")
opc = int(input("Elige una opcion: \n 1. Rutas de EXPORTACIÓN \n 2. Rutas IMPORTACIÓN \n"))

#Si se elige la opción 1, entonces se mostraran los resultados para las rutas de exportación
if opc ==1 :
    
    direccion = "Exports"
    bandera = 0
    rutas_contadas = []
    rutas_finales = []
    
    
    for ruta in lista_datos:
        #filtrar rutas de exportación
        if ruta [1] == direccion:
            #print(ruta)
            ruta_actual = [ruta[2], ruta[3]]
            
            #Iterar en las rutas que no esten contenidas en la variable rutas contadas
            #e irlas guardando en dicha variable, y mediante la variable bandera sumar el valor.
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2], movimiento [3]]:
                        bandera += int(movimiento[9])
     
                
                rutas_contadas.append(ruta_actual)
                rutas_finales.append([ruta[2], ruta[3], bandera])
                bandera = 0
        #ordenar de mayor a menor.                
    rutas_finales.sort(reverse = True, key = lambda x: x[2])
    print ("\n__________Las 10 mejores rutas de EXPORTACIÓN son: _________\n")
    print(rutas_finales[0:10])

#Si se elige la opción 2, entonces se mostraran los resultados para las rutas de importación
elif opc ==2:
    
    direccion = "Imports"
    bandera = 0
    rutas_contadas = []
    rutas_finales = []
    
    
    for ruta in lista_datos:
        #filtrar rutas de exportación
        if ruta [1] == direccion:
            #print(ruta)
            ruta_actual = [ruta[2], ruta[3]]
            
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2], movimiento [3]]:
                        bandera += int(movimiento[9])
     
                
                rutas_contadas.append(ruta_actual)
                rutas_finales.append([ruta[2], ruta[3], bandera])
                bandera = 0
                        
    rutas_finales.sort(reverse = True, key = lambda x: x[2])
    print ("\n_________Las 10 mejores rutas de IMPORTACION son: ________\n")
    print(rutas_finales[0:10])
    
#En caso de que se elija una opción distinta a exportación ó importación, entonces, se le mostrara
#un mensaje para que lo intente de nuevo, hasta que seleccione las opciones disponibles.

else: 
    print("Opción no disponible. Intenta nuevamente")
