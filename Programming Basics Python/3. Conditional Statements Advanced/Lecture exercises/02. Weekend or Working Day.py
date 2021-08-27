# Напишете програма която, чете ден от седмицата (текст),
# на английски език - въведен от потребителя.Ако денят е работен отпечатва на конзолата
# - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата да се отпечата
# - "Error".

# input:
# Monday
# expected output:
# Working day

# input:
# Sunday
# expected output:
# Weekend

# input:
# April
# expected output:
# Error


day_of_week = input()
if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    print("Working day")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    print("Weekend")
else:
    print("Error")