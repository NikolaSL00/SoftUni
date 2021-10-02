# Write a program that generates all the possible expressions and their results between a given list of numbers (integers) using only the + and - operators. Print them on the console, as shown in the example.

# INPUT:
# 1, 2

# OUTPUT:
# +1+2=3
# +1-2=-1
# -1+2=1
# -1-2=-3

# INPUT:
# 1, 1, 1, 1

# OUTPUT:
# +1+1+1+1=4
# +1+1+1-1=2
# +1+1-1+1=2
# +1+1-1-1=0
# +1-1+1+1=2
# +1-1+1-1=0
# +1-1-1+1=0
# +1-1-1-1=-2
# -1+1+1+1=2
# -1+1+1-1=0
# -1+1-1+1=0
# -1+1-1-1=-2
# -1-1+1+1=0
# -1-1+1-1=-2
# -1-1-1+1=-2
# -1-1-1-1=-4

def expressions(numbers, current_result, expression=""):
    if not numbers:
        return [(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f"{expression}+{numbers[0]}")
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f"{expression}-{numbers[0]}")
    return result_minus + result_plus


string = list([int(x) for x in input().split(", ")])
result = expressions(string, 0)
[print(f"{exp_str}={exp_result}") for (exp_str, exp_result) in result]
