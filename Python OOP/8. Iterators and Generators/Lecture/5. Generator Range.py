def genrange(param, param1):
    while param <= param1:
        yield param
        param += 1


print(list(genrange(1, 10)))
