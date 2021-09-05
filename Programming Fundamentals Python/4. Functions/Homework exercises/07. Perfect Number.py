# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Write a function which receives an integer number and returns one of the following messages:
# "We have a perfect number!" - if the number is perfect.
# "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.


# INPUT:
# 6

# EXPECTED OUTPUT:
#  We have a perfect number!


# INPUT:
# 28

# EXPECTED OUTPUT:
#  We have a perfect number!

def is_it_perfect(number):
    sum = 0
    if number % 2 == 0:
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                sum += i
    else:
        for i in range(1, (number - 1) // 2 + 1):
            if number % i == 0:
                sum += i
    if sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(is_it_perfect(number))
