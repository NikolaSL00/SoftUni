# You are at the zoo and the meerkats look strange.
# You will receive 3 strings: (tail, body, head).
# Your task is to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail).

# INPUT:
# my tail
# my body seems on place
# my head is on the wrong end!

# EXPECTED OUTPUT:
# ['my head is on the wrong end!','my body seems on place','my tail']


# INPUT:
# tail
# body
# head

# EXPECTED OUTPUT:
# ['head', 'body', 'tail']

tail = input()
body = input()
head = input()
list = [head, body, tail]
print(list)
