# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	    12	    14	        14	        12	       16	    16

# input:
# Monday
# expected output:
# 12

# input:
# Friday
# expected output:
# 12

# input:
# Sunday
# expected output:
# 16

day = input()

if day == "Monday" or day == "Friday" or day == "Tuesday":
    print(12)
elif day == "Wednesday" or day == "Thursday":
    print(14)
elif day == "Saturday" or day == "Sunday":
    print(16)