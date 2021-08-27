# Дадено число е валидно, ако е в диапазона [100…200] или е 0.
# Да се напише програма, която чете цяло число, въведено от потребителя,
# и печата "invalid" ако въведеното число не е валидно.

# input:
# 75
# expected output:
# invalid

# input:
# 150
# expected output:
# (няма изход)

# input:
# 220
# expected output:
# invalid

number = int(input())

if (number < 100 or number > 200) and number != 0:
    print("invalid")