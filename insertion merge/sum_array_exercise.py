#pseudocodigo del ejercicio.
"""SUM-ARRAY(A, n)
1 sum = 0
2 for i = 1 to n
3   sum = sum + A[i]
4 return sum"""

array = [1,2,3,4,5,6]

#traslado a código.
def sum_array(A):
    sum = 0
    n = len(A)
    for i in range(n):
        sum += A[i] # estamos iterando por todos los indices del array.
    return sum


print(sum_array(array))
# La invariante de ciclo sería:
# “Al inicio de cada iteración del bucle, la variable sum es igual a la suma de los primeros i elementos del array A.”

"""*Inicialización: Antes de la primera iteración (cuando i = 0), sum es 0, 
que es la suma de los primeros 0 elementos.

*Mantenimiento: Si la invariante es verdadera antes de una iteración del bucle, 
sigue siendo verdadera antes de la siguiente iteración. En cada paso, añadimos A[i] a sum, 
por lo que sum es siempre la suma de los primeros i+1 elementos después de la i-ésima iteración.

*Terminación: Al final del bucle, cuando i = n, la invariante nos dice que sum es igual 
a la suma de los primeros n elementos del array, que es exactamente lo que queremos demostrar."""


