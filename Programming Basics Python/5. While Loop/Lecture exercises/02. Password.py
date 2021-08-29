# Напишете програма, която първоначално прочита име и парола на потребителски профил.
# След това чете парола за вход, при въвеждане на грешна парола, потребителя да се подкани да въведе нова парола.

# input:
# Nakov
# 1234
# pass
# 1324
# 1234
# expected output:
# Welcome Nakov!

# input:
# Gosho
# secret
# secret
# expected output:
# Welcome Gosho!

username = input()
password = input()

tried = input()
while password != tried:
    tried = input()
else:
    print(f"Welcome {username}!")
