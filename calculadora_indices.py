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
def calcular_calorias_en_actividad(TMB: float,valor_actividad: float)->float:
    
    calorias_actividad=TMB*valor_actividad

    
    return calorias_actividad


"""

Calcula el rango de calorías recomendado, que debe consumir una persona 
diariamente en caso de que desee adelgazar, a partir de la ecuación 
definida anteriormente
"""
def consumo_calorias_recomendado_para_adelgazar(TMB:float , opcion:int)->str:

    mensaje=""  
    
    tmb1=TMB-(TMB*0.15)
    
    tmb2=TMB-(TMB*0.20)
    
    tmb3=TMB*0.8
    
    tmb4=TMB*0.85

    if opcion == 1:
        
        mensaje="Debe de consumir entre : " + str(tmb1) + " y "+  str(tmb2) + "calorias"
        
    else:
        mensaje="Debe consumir entre : " + str(tmb3) + " y " + str(tmb4) 
        
    


    return mensaje;





altura=1.75

peso=3

valor_genero=1



edad=20


IMC=calcular_IMC(peso, altura)


caloria_reposo=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)


print(caloria_reposo)

TMB=5.0

valor_actividad=3

calorias_actividad=calcular_calorias_en_actividad(TMB, valor_actividad)

opcion=1

consumo_adelgazar=consumo_calorias_recomendado_para_adelgazar(TMB, opcion)


print(consumo_adelgazar)




