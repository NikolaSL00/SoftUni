# You will receive a single integer number between 0 and 100 (inclusive) which is divisible by 10 without
# remainder (0, 10, 20, 30...). Your task is to create a function which returns a loading bar depending
# on the number you have received in the input. Print the result on the console. For more clarification
# see the examples below.

# INPUT:
# 30

# EXPECTED OUTPUT:
# 30% [%%%.......]
# Still loading...


# INPUT:
# 50

# EXPECTED OUTPUT:
# 50% [%%%%%.....]
# Still loading...

def loading_bar(number):
    count = number // 10
    print(f"{number}%", end=" ")
    if count < 10:
        print("[", end="")
        print("%" * count, end="")
        print("." * (10 - count), end="")
        print("]")
        print("Still loading...")
    elif count == 10:
        print("Complete!")
        print("[", end="")
        print("%" * count, end="")
        print("]")


number = int(input())

loading_bar(number)
