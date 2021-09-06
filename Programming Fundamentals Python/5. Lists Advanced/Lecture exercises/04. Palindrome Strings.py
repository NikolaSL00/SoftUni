# On the first line you will receive words separated by a single space.
# On the second line you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
#
# "Found palindrome {number} times".

# INPUT:
# wow father mom wow shirt stats
# wow

# EXPECTED OUTPUT:
# ['wow', 'mom', 'wow', 'stats']
# Found palindrome 2 times


# INPUT:
# hey how you doin? lol
# mom

# EXPECTED OUTPUT:
# ['lol']
# Found palindrome 0 times


separated_words = input().split(" ")
palindrome_word = input()

only_palindromes = [el for el in separated_words if el == el[::-1]]

print(only_palindromes)
print(f"Found palindrome {only_palindromes.count(palindrome_word)} times")
