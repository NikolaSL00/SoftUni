# You are given a file called numbers.txt with the following content:
#
# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

file = open("numbers.txt", "r")
sum = 0
for line in file:
    number = int(line)
    sum += number
print(sum)
