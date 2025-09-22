import math

def sumar_lista(numeros, i=0):
    if i == len(numeros): 
        return 0
    else:
        return numeros[i] + sumar_lista(numeros, i+1)

def contar_digitos(n):
    
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

def eliminarElementoMedio(pila, contador):
    elementoActual = pila.pop()
    
    if not pila:  
        pila.append(elementoActual)
        return math.ceil(contador / 2)  
    mitad = eliminarElementoMedio(pila, contador + 1)

    if contador!= mitad:  
        pila.append(elementoActual)

    return mitad

def es_palindromo(cadena):
   
    cadena = cadena.lower().replace(" ", "")

    if len(cadena) <= 1:
        return True

    if cadena[0] == cadena[-1]:

        return es_palindromo(cadena[1:-1])
    else:
        return False


if __name__ == "__main__":
   frase = "Anita lava la tina"
if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
