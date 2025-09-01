def solucionHash(lista, k):
    dic = {}        
    meta = 0

    for i in range(len(lista)):
        
        complemento = k - lista[i]

        if complemento in dic:
            print("solucion encontrada en el par:")
            print(f"{lista[i]} en la posición: {i}")
            print(f"{complemento} en la posición: {dic[complemento]}")
            meta+=1
        else:
            dic[lista[i]] = i
    
    if meta == 0:
        print("Solucion no encontrada")
    
    return meta


if __name__ == "__main__":

    entrada = input("Ingresa la lista de numeros: ") 
    lista = list(map(int, entrada.split()))
    k = int(input("Ingresa el valor k: "))
    solucionHash(lista, k)

