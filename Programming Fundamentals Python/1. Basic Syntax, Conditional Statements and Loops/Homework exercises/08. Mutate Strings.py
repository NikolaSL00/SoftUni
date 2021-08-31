# You will be given two strings. Transform the first string into the second one,
# one letter at a time and print it. Print only the unique strings.
# Note: the strings will have the same lengths.


# INPUT:
# bubble gum
# turtle hum

# EXPECTED OUTPUT:
# tubble gum
# turble gum
# turtle gum
# turtle hum


# INPUT:
# Kitty
# Doggy

# EXPECTED OUTPUT:
# Ditty
# Dotty
# Dogty
# Doggy


string1 = input()
string2 = input()
last_string = string1
for symbol in range(len(string1)):
    left_part = string2[:symbol + 1]
    right_part = string1[symbol + 1:]
    new_string = left_part + right_part
    if new_string == last_string:
        continue
    print(new_string)
    last_string = new_string
