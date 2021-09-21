# Write program that:
# Reads an input string
# Reverses it using a stack
# Prints the result back on the console

# Input:
# I Love Python

# Expected Output:
# nohtyP evoL I

# Input:
# Stacks and Queues

# Expected Output:
# seueuQ dna skcatS

input_string = input()
list_as_stack = []

for character in input_string:
    list_as_stack.append(character)

for _ in range(len(list_as_stack)):
    print(list_as_stack.pop(), end="")
