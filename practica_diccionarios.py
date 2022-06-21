# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 19:19:50 2022

@author: jorge
"""

pelicula1 = {
     "nombre":"Matriz 1",
     "genero":"Acción,Drama",
     "duracion":123,
     "anio":2000,
     "clasificacion":18,
     "hora":1620,
     "dia":"lunes"
 }


pelicula2 = {
     "nombre":"Harry potter 1",
     "genero":"Drama,Familia",
     "duracion":200,
     "anio":2001,
     "clasificacion":13,
     "hora":2000,
     "dia":"miercoles"
 }

pelicula3 = {
     "nombre":"El ciclista",
     "genero":"Drama,Familia,Deporte",
     "duracion":150,
     "anio":2019,
     "clasificacion":16,
     "hora":1700,
     "dia":"Viernes"
 }

def obtenerDuracionPromedio():
    
    global pelicula1
    global pelicula2
    global pelicula3
    
    duracion1=0
    duracion2=0
    duracion3=0
    total=0
    
    duracion1=obtenerDuracionPelicula(pelicula1)
    
    duracion2=obtenerDuracionPelicula(pelicula2)
    
    duracion3=obtenerDuracionPelicula(pelicula3)
    
    total=duracion1+duracion2+duracion3
    
    total=total/3
    
    return total

def obtenerDuracionPelicula(pelicula:dict)-> int:
    
    acumDuracion=0
    
    for clave in pelicula:
        
        if clave == "duracion" :
        
            acumDuracion=acumDuracion+pelicula[clave]
        

    return acumDuracion

print(obtenerDuracionPromedio())
