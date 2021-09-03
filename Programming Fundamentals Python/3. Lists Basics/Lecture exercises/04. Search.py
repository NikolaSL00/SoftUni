# You will receive a number n and a word.
# On the next n lines you will be given some strings.
# You should add them in a list and print them.
# After that you should filter out only the strings that include the given word and print that list too.

# INPUT:
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni

# EXPECTED OUTPUT:
# ['I study at SoftUni', 'I walk to work', 'I learn Python at SoftUni']
# ['I study at SoftUni', 'I learn Python at SoftUni']


# INPUT:
# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes

# EXPECTED OUTPUT:
# ['I love tomatoes', 'I can eat tomatoes forever', "I don't like apples", 'Yesterday I ate two tomatoes']
# ['I love tomatoes', 'I can eat tomatoes forever', 'Yesterday I ate two tomatoes']

n = int(input())
word = input()

list = []

for _ in range(0, n):
    list_words = input()
    list.append(list_words)
print(list)

list_2 = []
for words in list:
    if word in words:
        list_2.append(words)
print(list_2)
