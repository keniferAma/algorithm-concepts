"""Input: A sequence of n numbers 〈a1, a2, … , an〉 stored in array A[1 : n]
and a value x.
Output: An index i such that x equals A[i] or the special value NIL if x
does not appear in A."""

def exercise(A, x):
    n = len(A)
    for i in range(n):
        if x == A[i]:
            return i
    else:
        return "NIL"


array = [1,2,3,4,5,6,7]
print(exercise(array, 5))

# loop invariant hecho por la inteligencia artificial:
def ejercicio(A, x):
    n = len(A)
    for i in range(n):
        # Invariante de bucle: Después de la i-ésima iteración del bucle,
        # el elemento x no se ha encontrado en las primeras i posiciones del array A.
        if x == A[i]:
            return i
    # Si llegamos a este punto, significa que hemos examinado todos los elementos
    # del array y no hemos encontrado x, por lo que retornamos "NIL".
    return "NIL"



# version resuelta por la inteligencia artificial:

def encontrar_indice(A, x):
    try:
        i = A.index(x)
        return i
    except ValueError:
        return "NIL"


# Another version made by me.
def encontrar_indice_v2(A, x):
    if x in A:
        return A.index(x)
    else:
        return "NIL"
    
print(encontrar_indice_v2(array, 5))




A = [1,0,0,1,0,1,0,0,1]
B = [0,1,0,1,0,1,1,0,1]


def ADD_BINARY_INTEGERS(A, B, n):
    C = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, -1, -1):
        C[i + 1] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
        print(C)
    C[0] = carry
    return C

print(ADD_BINARY_INTEGERS(A, B, 6))

