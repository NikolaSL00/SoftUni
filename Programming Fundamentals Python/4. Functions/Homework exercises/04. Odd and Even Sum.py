# You will receive a single number. You should write a function that returns the sum of all even
# and the sum of all odd digits in the given number as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

# Print the result of the function on the console.


# INPUT:
#  1000435

# EXPECTED OUTPUT:
#  Odd sum = 9, Even sum = 4


# INPUT:
# 3495892137259234

# EXPECTED OUTPUT:
#  Odd sum = 54, Even sum = 22

def sum_of_odd_and_even_digits(num):
    sum_odd = 0
    sum_even = 0
    for digit in range(0, len(num)):
        if int(num[digit]) % 2 == 0:
            sum_even += int(num[digit])
        else:
            sum_odd += int(num[digit])
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number_as_string = input()

print(sum_of_odd_and_even_digits(number_as_string))
