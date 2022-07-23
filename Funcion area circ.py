# Realiza una función llamada area_circulo() que devuelva el área de
# un círculo a partir de un radio. Calcula el área de un círculo de 
# 5 de radio
import math #Importamos módulo math

def area_circulo(radio:int): #Definimos funcion
    
    return round(math.pi * (radio**2),3) #Realizamos operación y retornamos área

print(area_circulo(5)) #Mostramos en pantalla circulo de radio 5