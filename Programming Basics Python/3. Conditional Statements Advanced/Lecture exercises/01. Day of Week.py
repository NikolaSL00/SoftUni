# Напишете програма, която чете цяло число, въведено от потребителя,
# и отпечатва ден от седмицата (на английски език), в граници [1...7] или отпечатва "Error" в случай,
# че въведеното число е невалидно.

# input:
# 1
# expected output:
# Monday

# input:
# 2
# expected output:
# Tuesday

# input:
# -1
# expected output:
# Error

number = int(input())

if 0 < number < 8:
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
else:
    print("Error")