def squares(param):
    num = 1
    while param >= num:
        yield num ** 2
        num += 1


print(list(squares(5)))

# Output:
# [1, 4, 9, 16, 25]
