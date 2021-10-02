# Write a function called get_info that receives a name, an age, and a town and returns a string in the format:
# "This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function. Submit only the function in the judge system.


# Test Code:
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

# OUTPUT:
# This is George from Sofia and he is 20 years old


def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
