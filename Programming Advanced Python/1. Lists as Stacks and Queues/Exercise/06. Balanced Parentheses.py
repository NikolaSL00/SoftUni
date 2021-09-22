# You will be given a sequence consisting of parentheses.
# Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding
# closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].

# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.

# Input
# On a single line you will receive a sequence of parentheses.

# Output
# For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO". Do not print the quotes.

# Constraints
# 1 ≤ lens ≤ 1000, where lens is the length of the sequence.
# Each character of the sequence will be one of {, }, (, ), [, ].

# INPUT:
# {[()]}

# OUTPUT:
# YES

# INPUT:
# {[(])}

# OUTPUT:
# NO

# INPUT:
# {{[[(())]]}}

# OUTPUT:
# YES

stack_of_parentheses = []

input_string = input()
is_balanced = True
for char in input_string:
    if char in "([{":
        stack_of_parentheses.append(char)
    else:
        if stack_of_parentheses:
            last_opening_bracket = stack_of_parentheses.pop()
        else:
            is_balanced = False
            break
        pair = f'{last_opening_bracket}{char}'
        if pair not in "(){}[]":
            is_balanced = False
            break

if is_balanced and not stack_of_parentheses:
    print("YES")
else:
    print("NO")
