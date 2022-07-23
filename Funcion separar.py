# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares, y la segunda con los números impares:

def separar(lista:list): #Definimos función
    lista_pares = [] #Creamos lista pares
    lista_impares = [] #Creamos lista impares
    
    for i in lista: #Iteramos lista
        if i % 2 == 0: #Si el residuo de dividirlo entre 2 es 0, es par
            lista_pares.append(i) #Lo añadimos a la lista par
        
        else: #De lo contrario, es impar
            lista_impares.append(i) #Entonces lo añadimos a la lista impar
    
    lista_pares.sort() #Con el método sort.() ordenamos las listas
    lista_impares.sort()

    return lista_pares, lista_impares #Devolvemos una tupla con ambas listas como elementos

pares, impares = separar([6,5,2,1,7])

print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
