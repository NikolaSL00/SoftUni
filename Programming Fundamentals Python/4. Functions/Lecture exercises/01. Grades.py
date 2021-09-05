# Write a function which receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# ⦁	2.00 – 2.99 - "Fail"
# ⦁	3.00 – 3.49 - "Poor"
# ⦁	3.50 – 4.49 - "Good"
# ⦁	4.50 – 5.49 - "Very Good"
# ⦁	5.50 – 6.00 - "Excellent"

# INPUT:
# 3.33

# EXPECTED OUTPUT:
# Poor


# INPUT:
# 4.50

# EXPECTED OUTPUT:
# Very Good


# INPUT:
# 2.99

# EXPECTED OUTPUT:
# Fail

def grade_to_text(par):
    if 2 <= par <= 2.99:
        return "Fail"
    elif 3 <= par <= 3.49:
        return "Poor"
    elif 3.50 <= par <= 4.49:
        return "Good"
    elif 4.50 <= par <= 5.49:
        return "Very good"
    elif 5.50 <= par <= 6.00:
        return "Excellent"


a = float(input())

result = grade_to_text(a)
print(result)
