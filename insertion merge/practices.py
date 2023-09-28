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

array = [5, 7, 9, 3, 1, 3, 7]
print(insertio_sort_repaso(array=array))



# Ahora vamos a tratar de replicar el merge sort:

A1 = [9, 7, 5, 2]
A2 = [7, 5, 3, 1]

def merge(array_1, array_2):
    result = [9, 7, 5, 5, 7, 2, 3, 1]
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

print(merge(array_1=A1, array_2=A2))
