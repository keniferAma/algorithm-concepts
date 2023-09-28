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