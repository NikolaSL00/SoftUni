# You are given an algebraic expression with parentheses.
# Scan through the string and extract each set of parentheses.

# Print the result back on the console.




expression = input()
parentheses_indices = []

index = 0

for char in expression:

    if char == ")" and len(parentheses_indices) > 0:
        print(expression[parentheses_indices.pop():index + 1])
    elif char == "(" and char != expression[-1]:
        parentheses_indices.append(index)
    index += 1
