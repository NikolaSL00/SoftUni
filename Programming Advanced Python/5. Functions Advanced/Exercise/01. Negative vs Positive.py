# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
# On the first line, print the sum of the negatives
# On the second line, print the sum of the positives
# On the third line:
# If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.

# INPUT:
# 1 2 -3 -4 65 -98 12 57 -84

# OUTPUT:
# -189
# 137
# The negatives are stronger than the positives

# INPUT:
# 1 2 3

# OUTPUT:
# 0
# 6
# The positives are stronger than the negatives


def even_odd_operations(args):
    negative_sum = 0
    positive_sum = 0

    for number in args:
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) <= positive_sum:
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
even_odd_operations(numbers)
