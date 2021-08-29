# Напишете програма, която чете число n, въведено от потребителя,
# и отпечатва числата от 1 до n през 3 (със стъпка 3).

# input:
# 10
# expected output:
# 1
# 4
# 7
# 10

# input:
# 7
# expected output:
# 1
# 4
# 7

n = int(input())
for number in range(1, n + 1, +3):
    print(number)
