# Create a function called age_assignment that receives a different number of names and a different number of key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its first letter in the key-value pairs for each name and assign the age to the person's name. It the end, return a dictionary with all the names and ages as shown in the example. Submit only the function in the judge system.

# Test Code:
# print(age_assignment("Peter", "George", G=26, P=19))

# OUTPUT:
# {'Peter': 19, 'George': 26}

# Test Code:
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# OUTPUT:
# {'Amy': 22, 'Bill': 61, 'Willy': 36}

def age_assignment(*args, **kwargs):
    result_dict = {}
    for man in args:
        key = man[0]
        result_dict[man] = kwargs[key]
    return result_dict

