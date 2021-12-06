# Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list.

# Test Code:
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Desired Output:
# [2, 3, 5]

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    if num > 1:
        return True


def get_primes(param):
    primes = filter(lambda n: is_prime(n), param)
    for num in primes:
        yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
