# Implementando el algoritmo binary search:
# El siguiente algoritmo fue implementado por mí:
# Basicamente lo que hace este algoritmo es buscar algún elemento  y retornar su índice mediante divide y vencerás-
# Sin embargo en este ejemplo no lo hicimos mediante recursividad.
# DEBEMOS TENER EN CUENTA QUE ESTE ALGORITMO SOLAMENTE ES POSIBLE CON LISTAS ORGANIZADAS.

def binary_search(A, target):
    left = 0
    right = len(A) - 1

    while left <= right:
        half = right - left // 2
        
        if A[half] == target:
            return f"yes, it's index is {half}"

        elif A[half] < target:
            left = A.index(A[half + 1])

        else:
            right = A.index(A[half - 1])

    return "Element not found" 
    

array = [1,5,7,8,9,11,20,21,26,30]
target = 3
print(binary_search(array, target))




# El siguiente es el mismo algoritmo pero implementado por la inteligencia artificial:
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Verifica si el elemento medio es el objetivo
        if arr[mid] == target:
            return mid

        # Si el objetivo está en la mitad izquierda, descarta la mitad derecha
        elif arr[mid] > target:
            right = mid - 1

        # Si el objetivo está en la mitad derecha, descarta la mitad izquierda
        else:
            left = mid + 1

    # Si el objetivo no está presente en el arreglo
    return -1

# Ejemplo de uso
arr = [2, 3, 6, 8, 10, 15, 18]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"El elemento {target} está en la posición {result}.")
else:
    print(f"El elemento {target} no está presente en el arreglo.")
