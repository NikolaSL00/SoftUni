# Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
# Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.

# input ->    22
# expected output ->  39.50078

# input ->   100
# expected output ->  179.549

# input ->   12.5
# expected output ->  22.443625

usd = float(input())
BGN = usd * 1.79549
print(BGN)