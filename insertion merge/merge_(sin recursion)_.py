A = [5, 6, 9, 1, 3, 2, 7, 6, 10, 4]
R = [1, 3, 5, 6, 9] # asumiendo que estos subarray ya vienen ordenados desde su base por medio de la recursividad.
L = [2, 4, 7, 8, 10]
	
i = 0
j = 0
k = 0 # Aquí se ubica nuestro primer indice del array original, en el pseudocódigo sería la letra p, por cuestion 
# de ejecución lo asignamos en cero.
	
while i < len(L) and j < len(R): # comparacion hasta que se termine cualquiera de los dos array.
    if L[i] < R[j]:
        A[k] = L[i]
        i += 1
    
    else:
        A[k] = R[j]
        j += 1
        
    k += 1

# El fin de estos dos bucles es terminar el array restante que nos queda del primer while.
while i < len(L): # por si a este array le hizo falta ejecutar elementos.
    A[k] = L[i]
    i += 1
    
while j < len(R): # por si a este array le hizo falta ejecutar elementos.
    A[k] = R[j]
    j += 1