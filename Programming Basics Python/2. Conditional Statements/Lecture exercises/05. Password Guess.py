# Да се напише програма, която чете парола (един ред с произволен текст),
# въведена от потребителя и проверява дали въведеното съвпада с фразата "s3cr3t!P@ssw0rd".
# При съвпадение да се изведе "Welcome". При несъвпадение да се изведе "Wrong password!".

# input:
# qwerty
# expected output:
# Wrong password!

# input:
# s3cr3t!P@ssw0rd
# expected output:
# Welcome

# input:
# s3cr3t!p@ss
# expected output:
# Wrong password!

password = input()

if password== "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")