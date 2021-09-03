# You will be given a number n. On the next n lines you will receive integers.
# You should create and print two lists:
# ⦁	One with all the positives (including 0) numbers
# ⦁	One with all the negatives numbers
# Finally, print the following message: "Count of positives: {count_positives}.
# Sum of negatives: {sum_of_negatives}"

# INPUT:
# 5
# 10
# 3
# 2
# -15
# -4

# EXPECTED OUTPUT:
# [10, 3, 2]
# [-15, -4]
# Count of positives: 3. Sum of negatives: -19

number_n = int(input())

non_negative_int_list = []
negative_int_list = []

for i in range(0, number_n):
    number = int(input())
    if number < 0:
        negative_int_list.append(number)
    else:
        non_negative_int_list.append(number)
print(non_negative_int_list)
print(negative_int_list)
print(f"Count of positives: {len(non_negative_int_list)}. Sum of negatives: {sum(negative_int_list)}")
