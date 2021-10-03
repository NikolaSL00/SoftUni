# Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.

# Test Code:
# print(palindrome("abcba", 0))

# OUTPUT:
# abcba is a palindrome

# Test Code:
# print(palindrome("peter", 0))

# OUTPUT:
# peter is not a palindrome

def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    if word[idx] != word[len(word) - 1 - idx]:
        return f"{word} is not a palindrome"
    return palindrome(word, idx + 1)
