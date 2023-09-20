
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
        baraja[left_hand_index + 1] = right_hand
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