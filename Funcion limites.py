# Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, 
# el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(num:int, minimo:int, maximo:int): #Definimos función
    if num<minimo: #Si el número es menor al límite inferior, imprimimos el límite inferior
        return minimo
    
    elif num>maximo: #Si el número es mayor al límite superior, imprimimos el límite superior
        return maximo
    
    elif minimo <= num <= maximo: #Si numero está entre ambos límites, imprimimos el número
        return num

print(recortar(15, 0, 10))