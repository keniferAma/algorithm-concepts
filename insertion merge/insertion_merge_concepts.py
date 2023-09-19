
lista_de_elementos = [9, 56, 43, 67, 2, 0]

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


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