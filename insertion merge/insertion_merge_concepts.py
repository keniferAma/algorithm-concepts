
lista_de_elementos = [9, 56, 43, 67, 2, 0]

def insertion_sort(baraja):
    n = len(baraja)
    for carta in range(1, n):
        right_hand = baraja[carta]
        left_hand_index = carta - 1 # Estamos asumiendo que la primera carta ya se encuentra en la mano izquierda.
        while left_hand_index >= 0 and baraja[left_hand_index] > right_hand:
            baraja[left_hand_index + 1] = baraja[left_hand_index]
            left_hand_index -= 1
            # Este bucle while tiene una gran particularidad:
            # Primero lo que hace es convertir esa carta que es menor a la izquierda en dicha carta, luego devuelve el
            # index y esta vez vamos a comparar esa menor con el anterior.
            # Basicamente en este bucle estamos tratando de salir mediante que la carta derecha sea menor a la de las
            # de la izquierda.
            # Basicamente baraja[left_hand_index] debería salir de este bucle con espacio en blanco a su izquierda
            # con el fin de que right_hand sea asignado a la derecha del espacio en blanco.
            # (pasa a ser reemplazado)
        baraja[left_hand_index + 1] = right_hand # si sale del bucle satisfactoriamente, quiere decir que "right_hand"
        # sale menor que left_hand y por consiguiente se va a ubicar o bien sea al final izquierdo o a la derecha
        # del menor a él.
    return baraja


print(insertion_sort(lista_de_elementos))

"""Insertion sort works the way you
might sort a hand of playing cards. Start with an empty left hand and
the cards in a pile on the table. Pick up the first card in the pile and hold
it with your left hand. Then, with your right hand, remove one card at a
time from the pile, and insert it into the correct position in your left
hand. As Figure 2.1 illustrates, you find the correct position for a card
by comparing it with each of the cards already in your left hand,
starting at the right and moving left. As soon as you see a card in your
left hand whose value is less than or equal to the card you’re holding in
your right hand, insert the card that you’re holding in your right hand
just to the right of this card in your left hand. If all the cards in your left
hand have values greater than the card in your right hand, then place
this card as the leftmost card in your left hand. At all times, the cards
held in your left hand are sorted, and these cards were originally the top
cards of the pile on the table."""




# ahora vamos a intentar replicarlo


def insertion(lista):
    for n in range(1, len(lista)):
        key = lista[n]
        j = n - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key



# INVARIANTE DE BUCLE: 

# Es una sentencia que nos confirma antes y después de algún bucle que dicha condicion se cumple antes y despues de 
# ejecutarse dicho bucle. En nuestro ejemplo sería algo como: la sublista "lista[n - j]" siempre está ordenada de 
# forma ascendente, lo cual es cierto ya que cada vez que se ejecuta un ciclo del bucle for, ya tendremos un 
# nuevo elemento ordenado. Es como una sentencia o afirmación que nos ayuda a entender mejor los algoritmos y además 
# nos puede ayudar a saber si realmente nuestro algoritmo esta desempeñando la función para la cual fue creado.

"""*Initialization: It is true prior to the first iteration of the loop.
*Maintenance: If it is true before an iteration of the loop, it remains true
before the next iteration.
*Termination: The loop terminates, and when it terminates, the invariant
—usually along with the reason that the loop terminated—gives us a
useful property that helps show that the algorithm is correct."""




# Ejercicio tratando de invertir la funcion de insersion antes mencionada.
def insertion(lista):
    for n in range(1, len(lista)):
        key = lista[n]
        j = n - 1
        while j >= 0 and lista[j] < key:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key


lista_de_elementos = [9, 56, 43, 67, 2, 0]

insertion(lista_de_elementos)

print(lista_de_elementos)


