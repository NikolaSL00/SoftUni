class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        output = f"Function '{self.func.__name__}' was called. Result: {result}\n"
        with open('results.txt', 'a') as output_file:
            output_file.write(output)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
