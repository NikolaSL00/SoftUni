# Да се напише конзолна програма, която прочита възраст (реално число) и пол ('m' или 'f'),
# въведени от потребителя, и отпечатва обръщение измежду следните:
# ⦁	"Mr." – мъж (пол 'm') на 16 или повече години
# ⦁	"Master" – момче (пол 'm') под 16 години
# ⦁	"Ms." – жена (пол 'f') на 16 или повече години
# ⦁	"Miss" – момиче (пол 'f') под 16 години

# input:
# 12
# f
# expected output:
# Miss

# input:
# 17
# m
# expected output:
# Mr.

# input:
# 25
# f
# expected output:
# Ms.

age = float(input())
sex = input()

if sex == "m":
    if age < 16:
        print("Master")
    else:
        print("Mr.")
else:
    if age < 16:
        print("Miss")
    else:
        print("Ms.")


