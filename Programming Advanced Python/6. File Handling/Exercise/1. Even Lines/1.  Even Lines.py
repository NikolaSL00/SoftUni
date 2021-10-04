# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

# Example Input:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.

# Output:
# fault@ his wasn't it but him@ judge to quick was @I
# safer@ is It here@ hide @Quick@


from collections import deque

file = open("text.txt", "r")

count = 0
deque_lines = deque()
specialChars = "-,.!?"

for line in file:
    if count % 2 == 0:
        deque_lines.append(line.strip())
    count += 1

for line in deque_lines:
    words_of_line = line.split(" ")
    words_of_line.reverse()

    for index in range(len(words_of_line)):
        for specialChar in specialChars:
            words_of_line[index] = words_of_line[index].replace(specialChar, "@")
    print(" ".join(words_of_line))
file.close()

