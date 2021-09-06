# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)

# INPUT:
# 72olle 103doo 100ya

# EXPECTED OUTPUT:
# Hello good day

# INPUT:
# 82yade 115te 103o

# EXPECTED OUTPUT:
# Ready set go

secret_message = [el for el in input().split(" ")]


def decipher_func(ascii: int, el: str):
    digits_str = ''
    for index in range(len(el)):
        if el[index].isdigit():
            digits_str += el[index]
    new_word = []
    new_word.append(chr(int(digits_str)))
    for index in range(ascii, len(el)):
        new_word.append(el[index])
    return new_word


for el in secret_message:
    if el[0].isdigit():
        ascii_numb = 1
        if el[1].isdigit():
            ascii_numb = 2
            if el[2].isdigit():
                ascii_numb = 3

    word = decipher_func(ascii_numb, el)
    word[1], word[-1] = word[-1], word[1]
    print("".join(word), end=" ")
