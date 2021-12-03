def reverse_text(param):
    start = len(param) - 1
    while start >= 0:
        yield param[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')
