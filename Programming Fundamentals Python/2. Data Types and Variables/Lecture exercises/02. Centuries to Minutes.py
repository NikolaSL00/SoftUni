# Write a program which reads an integer number of centuries and converts it to years, days, hours and minutes.

# INPUT:
# 1

# EXPECTED OUTPUT:
# 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes


# INPUT:
# 5

# EXPECTED OUTPUT:
# 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes

century = int(input())
years = century * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
