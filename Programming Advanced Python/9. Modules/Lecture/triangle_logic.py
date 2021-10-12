def print_line(n):
    for i in range(1, n + 1):
        for i1 in range(1, i + 1):
            print(i1, end="")
        print()

    for i in range(n, 1, -1):
        for i1 in range(1, i):
            print(i1, end="")
        print()