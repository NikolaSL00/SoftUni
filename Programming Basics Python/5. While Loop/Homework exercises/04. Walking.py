# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня
# и когато постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла
# "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

# input:
# 1000
# 1500
# 2000
# 6500
# expected output:
# Goal reached! Good job!
# 1000 steps over the goal!

# input:
# 1500
# 3000
# 250
# 1548
# 2000
# Going home
# 2000
# expected output:
# Goal reached! Good job!
# 298 steps over the goal!

steps_walked = 0
goal = 10000
command = input()
while command != "Going home":
    steps_walked += int(command)
    if goal > steps_walked:
        command = input()
    else:
        break
else:
    command = int(input())
    steps_walked += command

if goal > steps_walked:
    print(f"{goal - steps_walked} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps_walked - goal} steps over the goal!")
