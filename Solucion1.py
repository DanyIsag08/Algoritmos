def Busqueda(lista, k):
    meta = 0

    for i in range(len(lista)):                
        for j in range(i, len(lista)):   
            if lista[i] + lista[j] == k:
                print("Solución encontrada.")
                print(f"{lista[i]} en la posición: {i}")
                print(f"{lista[j]} en la posición: {j}")
                meta += 1
    
    if meta == 0:
        print("No se encontraron pares")

    return meta

if __name__ == "__main__":

    entrada = input("Ingresa la lista de numeros: ") 
    lista = list(map(int, entrada.split()))
    k = int(input("Ingresa el valor k: "))
    Busqueda(lista, k)
