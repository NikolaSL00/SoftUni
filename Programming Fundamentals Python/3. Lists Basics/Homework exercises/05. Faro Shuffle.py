# A faro shuffle is a method of shuffling deck of cards, in which the deck is split exactly in half
# and then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives
# a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

# INPUT:
# a b c d e f g h
# 5

# EXPECTED OUTPUT:
# ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']


# INPUT:
# one two three four
# 3

# EXPECTED OUTPUT:
# ['one', 'three', 'two', 'four']


string = input()

count_of_shuffles = int(input())

list_of_cards = string.split(" ")

middle_index = int(len(list_of_cards) / 2)
for _ in range(count_of_shuffles):
    first_half_deck = list_of_cards[:middle_index]
    second_half_deck = list_of_cards[middle_index:]
    list_of_cards = []
    for n in range(middle_index):
        list_of_cards.append(first_half_deck[n])
        list_of_cards.append(second_half_deck[n])
print(list_of_cards)
