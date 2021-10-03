# Create a function called kwargs_length() that can receive some keyword arguments and return their length. Submit only the function in the judge system.

# Test Code:
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))

# OUTPUT:
# 2

# Test Code:
# dictionary = {}
#
# print(kwargs_length(**dictionary))

# OUTPUT:
# 0


def kwargs_length(**kwargs):
    return len(kwargs)

