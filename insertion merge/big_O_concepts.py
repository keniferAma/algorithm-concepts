"""O(1) - Tiempo constante: Un algoritmo tiene un tiempo constante si siempre toma el mismo tiempo para ejecutarse, 
independientemente del tamaño de la entrada. Un ejemplo es acceder a un elemento en un array por su índice."""
def get_first_element(array):
    return array[0]



"""
O(n) - Tiempo lineal: Un algoritmo tiene un tiempo lineal si el tiempo de ejecución aumenta proporcionalmente 
con el tamaño de la entrada. Un ejemplo es encontrar el valor máximo en un array."""
def find_max(array):
    max_value = array[0]
    for num in array:
        if num > max_value:
            max_value = num
    return max_value



"""
O(log n) - Tiempo logarítmico: Un algoritmo tiene un tiempo logarítmico si el tiempo de ejecución aumenta 
logarítmicamente con el tamaño de la entrada. Un ejemplo es la búsqueda binaria."""
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1



"""
O(n^2) - Tiempo cuadrático: Un algoritmo tiene un tiempo cuadrático si el tiempo de ejecución aumenta 
proporcionalmente al cuadrado del tamaño de la entrada. Un ejemplo es la ordenación por burbuja."""
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



"""
O(n!) - Tiempo factorial: Un algoritmo tiene un tiempo factorial si el tiempo de ejecución aumenta 
factorialmente con el tamaño de la entrada. Un ejemplo es generar todas las permutaciones posibles de una lista."""
def generate_permutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    else:
        permutations = []
        for i in range(len(array)):
            rest = array[:i] + array[i+1:]
            for p in generate_permutations(rest):
                permutations.append([array[i]] + p)
        return permutations

