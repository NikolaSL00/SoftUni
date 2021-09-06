# Using a comprehension, write a program that receives some text,
# separated by space, and take only those words, whose length is even.
# Print each word on a new line.

# INPUT:
# kiwi orange banana apple

# EXPECTED OUTPUT:
# kiwi
# orange
# banana


# INPUT:
# pizza cake pasta chips

# EXPECTED OUTPUT:
# cake


words_input = [el for el in input().split(" ")]

words_with_even_length = [el for el in words_input if len(el) % 2 == 0]

print("\n".join(words_with_even_length))
