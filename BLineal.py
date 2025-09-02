def busqueda_lineal(lista, k):
    pasos = 0
    for elemento in lista:
        pasos += 1
        if elemento == k:
            return pasos 
    return pasos  

if __name__ == "__main__":

    entrada = input("Ingresa la lista de números: ") 
    lista = list(map(int, entrada.split())) 
    k = int(input("Ingresa el número que deseas buscar: "))
    
    comparaciones = busqueda_lineal(lista, k)
    
    if k in lista:
        print(f"El número {k} fue encontrado en {comparaciones} comparaciones.")
    else:
        print(f"El número {k} NO está en la lista. Se hicieron {comparaciones} comparaciones.")
