# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.


# input:
# 25
# expected output:
# 351

# input:
# 20
# expected output:
# 231

n = int(input())
combination_count = 0
for number in range(0, n + 1):
    for number1 in range(0, n + 1):
        for number2 in range(0, n + 1):
            if number + number1 + number2 == n:
                combination_count += 1
print(combination_count)
