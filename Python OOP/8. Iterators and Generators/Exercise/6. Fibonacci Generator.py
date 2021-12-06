# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely
# (starting from 0). Each Fibonacci number is created by the sum of the current number with the previous.


def fibonacci():
    # starting_numb = [0, 1]
    # yield starting_numb[0]
    # yield starting_numb[1]
    # while True:
    #     next_number = starting_numb[len(starting_numb) - 2] + starting_numb[len(starting_numb) - 1]
    #     starting_numb.append(next_number)
    #     yield next_number

    f1 = 0
    f2 = 1
    yield f1
    yield f2
    f_1 = f2
    f_2 = f1
    while True:
        fn = f_1 + f_2
        yield fn
        f_2 = f_1
        f_1 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
