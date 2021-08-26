# Да се напише програма, която чете цяло число,
# въведено от потребителя, и проверява, дали е под 100,
# между 100 и 200 или над 200. Да се отпечатат съответно съобщения, като в примерите по-долу:

# input:
# 95
# expected output:
# Less than 100

# input:
# 120
# expected output:
# Between 100 and 200

# input:
# 210
# expected output:
# Greater than 200

number = int(input())

if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")