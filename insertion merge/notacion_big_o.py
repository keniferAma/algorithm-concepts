"""Claro, aquí te dejo algunos ejemplos de código en Python que representan diferentes complejidades
 de tiempo Big O:"""
def es_par(n):
    return n % 2 == 0
# Este algoritmo tiene un tiempo de ejecución constante porque solo realiza una operación, 
# sin importar el tamaño de la entrada.



"""O(n) - Tiempo lineal:"""
def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

# Este algoritmo tiene un tiempo de ejecución lineal porque recorre cada elemento de la lista una vez.



"""O(n^2) - Tiempo cuadrático:"""
def ordenamiento_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Este algoritmo tiene un tiempo de ejecución cuadrático porque para cada elemento de la lista, recorre la lista nuevamente 
# para comparar los elementos.




"""O(log n) - Tiempo logarítmico:"""
def busqueda_binaria(lista, item):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        suposicion = lista[medio]
        if suposicion == item:
            return medio
        if suposicion > item:
            alto = medio - 1
        else:
            bajo = medio + 1
    return None

# Este algoritmo tiene un tiempo de ejecución logarítmico porque con cada iteración, 
# reduce a la mitad el número de elementos que necesita revisar.




"""O(n log n) - Tiempo lineal logarítmico:"""
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Este algoritmo tiene un tiempo de ejecución lineal logarítmico porque divide la lista en dos mitades 
# con cada iteración (log n), y luego realiza una operación para cada elemento en la lista (n).
