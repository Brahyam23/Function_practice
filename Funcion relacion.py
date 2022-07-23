# Realiza una función llamada relacion() que a partir de dos 
# números cumpla lo siguiente:

#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.

def relacion(num_1, num_2): #Definimos funcion
    if num_1>num_2: #Si el primer valor es mayor, retornamos 1
        return 1
    
    elif num_1<num_2: #Si el primer valor es menor, retornamos -1
        return -1
    
    else: #Si son iguales, retornamos un 0
        return 0

print(relacion(5, 5))