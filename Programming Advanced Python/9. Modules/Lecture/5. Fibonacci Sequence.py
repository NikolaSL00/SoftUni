from fibonacci_logic import create_sequence, locate

n = int(input("Enter the fibonacci number: "))
m = int(input("Enter the number we will search for:"))

try:
    print(create_sequence(n))
    print(locate(10))
except IndexError as err:
    print(err)
