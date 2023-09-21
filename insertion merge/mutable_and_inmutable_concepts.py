"""La razón por la que algunas variables modifican el valor original y otras no se debe a cómo los 
lenguajes de programación manejan diferentes tipos de datos.

En Python, los tipos de datos se dividen en dos categorías: inmutables y mutables.

Los tipos de datos inmutables incluyen enteros, flotantes, cadenas y tuplas. Cuando pasas una variable 
inmutable a una función, la función crea una copia de la variable y trabaja con esa copia. 
Por lo tanto, cualquier cambio que haga la función a la variable no afectará a la variable original.

Por otro lado, los tipos de datos mutables incluyen listas, diccionarios y conjuntos. 
Cuando pasas una variable mutable a una función, la función trabaja directamente con la variable original. 
Por lo tanto, cualquier cambio que haga la función a la variable se reflejará en la variable original.

Aquí tienes un ejemplo para cada tipo:"""

# Tipo de dato inmutable (entero)
def cambiar_entero(x):
    x = 100

a = 1
cambiar_entero(a)
print(a)  # Salida: 1

# Tipo de dato mutable (lista)
def cambiar_lista(x):
    x[0] = 100

b = [1, 2, 3]
cambiar_lista(b)
print(b)  # Salida: [100, 2, 3]



# Otro ejemplo:
def entero(v):
    v = 1
    return v

e = 5

print(entero(e))

print(e)