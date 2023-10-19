j = 0
total = []
for n in range(1, 5):
    s = [0] * n 
    n += 1
    total.append(s)

print(total)



# vamos a tratar de replicar un insertion sort:
def insertio_sort_repaso(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

array = [9, 7, 5, 5, 7, 2, 3, 1]
print(insertio_sort_repaso(array=array))



# Ahora vamos a tratar de replicar el merge sort:

A1 = [9, 7, 5, 2]
A2 = [7, 5, 3, 1]

def merge(original, array_1, array_2):
    result = original
    i = 0
    j = 0
    k = 0

    while i < len(array_1) and j < len(array_2):
        if array_1[i] > array_2[j]:
            result[k] = array_1[i]
            i += 1

        else:
            result[k] = array_2[j]
            j += 1

        k += 1
    while i < len(array_1):
        result[k] = array_1[i]
        i += 1
        k += 1
    
    while j < len(array_2):
        result[k] = array_2[j]
        j += 1
        k += 1

    return result



# Ahora vamos a tratar de replicar la función recursiva.

def merge_sort(A):
    n = len(A)
    middle = n // 2
    if n == 1:
        return [A[0]]

    right_array = merge_sort(A[middle:])
    left_array = merge_sort(A[:middle])

    return merge(A, right_array, left_array)

print(merge_sort(array))




# Es posible implementar el binary search con el insertion sort?

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j] # corremos una posición a la derecha la última del bloque organizado.
            # Al pasar eso, luego nuestro índice de "j" (los organizados) va un paso hacia atrás y nuevamente
            # comparamos con key.
            j -= 1

        array[j + 1] = key
    return array


array_binary = [1, 34, 2, 56, 7, 89, 0, 5]
print(insertion_sort(array_binary))




# Exercise 2.3-8:
"""Describe un algoritmo que, dado un conjunto S de n enteros y otro entero x, determine si S 
contiene dos elementos que suman exactamente x. Tu algoritmo debería tomar Θ(n lg n) tiempo en el 
peor de los casos."""
# Exercise done by me:


s = [2, 4, 4, 13, 3, 2, 7]
x = 9

def exercise(array, target):
    suma = 0
    for i in range(target, 0, -1):
        pares = (i, suma)
        suma += 1

        if pares[0] in array and pares[-1] in array:
            return "Yes"
        
    return "No"             

print(exercise(s, x))

