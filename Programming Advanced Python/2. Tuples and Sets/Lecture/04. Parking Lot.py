# Write a program that:
# Records a car number for every car that enters the parking lot
# Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N.
# On the following N lines, you will receive the direction and car's number in the format:
# "{direction}, {car_number}". The direction could only be "IN" or "OUT".
# Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique.
# If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter.

# INPUT:
# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

# OUTPUT:
# CA2844AA
# CA9999TT
# CA2822UU
# CA9876HH


# INPUT:
# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA

# OUTPUT:
# Parking Lot is Empty

number_of_commands = int(input())

parking = set()

for _ in range(number_of_commands):
    command, car_number = input().split(", ")
    if command == "IN":
        parking.add(car_number)
    elif command == "OUT":
        parking.remove(car_number)
if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
