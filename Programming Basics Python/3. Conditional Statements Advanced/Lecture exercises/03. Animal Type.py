# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
# ⦁	dog -> mammal
# ⦁	crocodile, tortoise, snake -> reptile
# ⦁	others -> unknown

# input:
# dog
# expected output:
# mammal

# input:
# snake
# expected output:
# reptile

# input:
# cat
# expected output:
# unknown

animal = input()

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")