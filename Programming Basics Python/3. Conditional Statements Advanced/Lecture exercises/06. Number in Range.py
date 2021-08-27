# Да се напише програма, която проверява дали въведеното от потребителя число е в интервала [-100, 100]
# и е различно от 0 и извежда "Yes", ако отговаря на условията, или "No" ако е извън тях.

# input:
# -25
# expected output:
# Yes

# input:
# 0
# expected output:
# No

# input:
# 25
# expected output:
# Yes

number = int(input())

if -100 <= number <= 100 and number != 0:
    print("Yes")
else:
    print("No")
