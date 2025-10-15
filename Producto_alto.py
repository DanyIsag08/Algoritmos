A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

max_producto = 0 
num1 = 0
num2 = 0

for i in range(len(A)):
    for j in range(i+1, len(A)): 
        producto = A[i] * A[j]
        if producto > max_producto:
            max_producto = producto
            num1 = A[i]
            num2 = A[j]

print("Los dos números con el mayor producto son:", num1, "y", num2)
print("Producto máximo:", max_producto)
