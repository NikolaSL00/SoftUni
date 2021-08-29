# Напишете програма, която чете текст(стринг),
# въведен от потребителя и печата всеки символ от текста на отделен ред.

# input:
# softuni
# expected output:
# s
# o
# f
# t
# u
# n
# i

text = input()
for number in range(0, len(text)):
    print(text[number])
