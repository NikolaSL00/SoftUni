# Using a dictionary comprehension, write a program which receives country names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", "). Print each country with their capital on a separate line in the following format:
# "{country} -> {capital}"

# INPUT:
# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London

# OUTPUT:
# Bulgaria -> Sofia
# Romania -> Bucharest
# Germany -> Berlin
# England -> London


list_of_countries = input().split(", ")
list_of_capitals = input().split(", ")

dictionary = dict(zip(list_of_countries, list_of_capitals))
for key, value in dictionary.items():
    print(f"{key} -> {value}")
