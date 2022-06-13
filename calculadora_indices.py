# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:51:00 2022

@author: jorge
"""


"""
Calcula el índice de masa corporal de una persona a partir de la ecuación
definida anteriormente
""" 
def calcular_IMC( peso: float, altura: float) -> float:
    
    
    
    return peso/(altura*altura)

"""
Calcula el porcentaje de grasa de una persona a partir de la ecuación 
definida anteriormente
"""
def calcular_porcentaje_grasa(peso: float,altura: float ,edad: int ,valor_genero: float,IMC: float):
    
    
    porcentaje_grasa_corporal=0.0
    
    porcentaje_grasa_corporal=1.2*IMC+0.23*edad-5.4-valor_genero
    
    
    
    return porcentaje_grasa_corporal


"""
Calcula la cantidad de calorías que una persona quema estando en reposo
(esto es, su tasa metabólica basal), a partir de la ecuación definida 
anteriormente.
"""
def calcular_calorias_en_reposo(peso: float,altura: float ,edad: int ,valor_genero: float):
    
    
    
    
    caloria_reposo= (10*peso)+(6.25*altura)-(5*edad)+valor_genero    
   
   
    return caloria_reposo
    


"""
Calcula la cantidad de calorías que una persona quema al realizar algún tipo 
de actividad física (esto es, su tasa metabólica basal según actividad física), 
a partir de la ecuación definida anteriormente
"""
def calcular_calorias_en_actividad(peso: float,altura: float ,edad: int ,valor_genero: float,valor_actividad: float):
    
    

    
    return float


"""

Calcula el rango de calorías recomendado, que debe consumir una persona 
diariamente en caso de que desee adelgazar, a partir de la ecuación 
definida anteriormente
"""
def consumo_calorias_recomendado_para_adelgazar():



    return float;





altura=1.75

peso=3

valor_genero=1



edad=20


IMC=calcular_IMC(peso, altura)


caloria_reposo=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)


print(caloria_reposo)

