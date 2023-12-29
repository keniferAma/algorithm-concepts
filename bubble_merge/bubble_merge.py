# trying to implement bubble merge by myself #

lista_de_prueba = [1, 3, 6, 7, 2, 20, 1, 3, 9]


def bubble(A):
    n = len(A)

    for j in range(n):
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                saved_number = A[i]
                A[i] = A[i + 1]
                A[i + 1] = saved_number
    
    return A

print(bubble(lista_de_prueba))