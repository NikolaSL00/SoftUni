# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

# input:
# 35
# 45
# 44
# expected output:
# 2:04

# input:
# 22
# 7
# 34
# expected output:
# 1:03

# input:
# 50
# 50
# 49
# expected output:
# 2:29

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

total_seconds = number_1 + number_2 + number_3
minutes = total_seconds // 60
seconds = total_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")