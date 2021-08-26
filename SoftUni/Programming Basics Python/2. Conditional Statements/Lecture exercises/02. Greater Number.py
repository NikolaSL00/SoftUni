# Да се напише програма, която чете две цели числа въведени от потребителя
# и отпечатва по-голямото от двете.

#input:
# 5
# 3
#expected output:
# 5

#input:
# 3
# 5
#expected output:
# 5

#input:
# 10
# 10
#expected output:
# 10


number = int(input())
number1 = int(input())

if number > number1:
    print(number)
elif number1 > number:
    print(number1)
else:
    print(number)
