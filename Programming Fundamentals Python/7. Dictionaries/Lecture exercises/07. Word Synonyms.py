# Write a program, which keeps a dictionary with synonyms. The key to the dictionary will be the word. The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words. After each word, you will be given a synonym, so the count of lines you should read from the console is 2 * n. You will be receiving a word and a synonym each on a separate line like this:
# ⦁	{word}
# ⦁	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2… synonymN}

# INPUT:
# 3
# cute
# adorable
# cute
# charming
# smart
# clever

# OUTPUT:
# cute - adorable, charming
# smart - clever

# INPUT:
# 2
# task
# problem
# task
# assignment

# OUTPUT:
# task - problem, assignment

n = int(input())

synonym_dict = dict()

for _ in range(n):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = list()
        synonym_dict[word].append(synonym)
    else:
        synonym_dict[word].append(synonym)

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")
