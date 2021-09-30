# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
# ⦁	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# ⦁	Columns + rows define the middle letter:
# ⦁	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# ⦁	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
# ⦁	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
# ⦁	r and c are integers in range [1, 26]

# INPUT:
# 4 6

# OUTPUT:
# aaa aba aca ada aea afa
# bbb bcb bdb beb bfb bgb
# ccc cdc cec cfc cgc chc
# ddd ded dfd dgd dhd did

# INPUT:
# 3 2

# OUTPUT:
# aaa aba
# bbb bcb
# ccc cdc

rows, columns = [int(x) for x in input().split()]

result_matrix = []
base = 97
for row in range(rows):
    row_c = []
    for column in range(columns):
        row_c.append(f"{chr(base + row)}{chr(base + column + row)}{chr(base + row)}")
    result_matrix.append(row_c)

for el in result_matrix:
    print(" ".join(el))
