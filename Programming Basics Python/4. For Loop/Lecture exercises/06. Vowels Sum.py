# Да се напише програма, която чете текст (стринг), въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:

# буква	    a	e	i	o	u
# стойност	1	2	3	4	5


# input:
# hello
# expected output:
# 6

# input:
# bamboo
# expected output:
# 9

text = input()
price = 0
for char in text:
    if char == "a":
        price += 1
    elif char == "e":
        price += 2
    elif char == "i":
        price += 3
    elif char == "o":
        price += 4
    elif char == "u":
        price += 5
print(price)
