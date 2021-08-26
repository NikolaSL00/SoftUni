# Да се напише програма, която чете цяло число,
# въведено от потребителя и отпечатва на конзолата дали числото е четно или нечетно.

# input:
# 2
# expected output:
# even

# input:
# 3
# expected output:
# odd

# input:
# 1024
# expected output:
# even

number = int(input())

if number % 2 == 0:
    print("even")
else:
    print("odd")