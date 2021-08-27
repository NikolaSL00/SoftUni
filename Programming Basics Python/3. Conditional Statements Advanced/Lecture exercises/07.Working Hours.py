# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст)
# - въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

# input:
# 11
# Monday
# expected output:
# open

# input:
# 19
# Friday
# expected output:
# closed

# input:
# 11
# Sunday
# expected output:
# closed

hour = int(input())
day = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")