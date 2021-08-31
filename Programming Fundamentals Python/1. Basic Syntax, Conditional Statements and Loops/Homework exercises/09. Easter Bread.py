# Since it is Easter you have decided to make some cozonacs and exchange them for eggs.
# Create a program that calculates how much cozonacs you can make with the budget you have.
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# Here is the recipe for one cozonac:

# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l

# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1l milk is 25% more than price for 1 kg flour.
# Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
# Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
# For every cozonac that you make, you will receive 3 colored eggs.
# For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received
# the usual 3 colored eggs for your cozonac.
# The count of eggs you will lose is calculated when you subtract 2 from your current count of cozonacs –
# ({currentCozonacsCount} – 2)
# In the end, print the cozonacs you made, the eggs you have gathered and the money you have left,
# formatted to the 2nd decimal place, in the following format:
# "You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."

# Input / Constraints
# On the 1st line you will receive the budget – a real number in the range [0.0…100000.0]
# On the 2nd line you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]
# The input will always be in the right format.
# You will always have a remaining budget.
# There will not be a case in which the eggs become a negative count.

# Output
# In the end print the count of cozonacs you have made, the colored eggs you have gathered,
# and the money formatted to the 2nd decimal place in the format described above.

# INPUT:
# 20.50
# 1.25

# EXPECTED OUTPUT:
# You made 7 cozonacs! Now you have 16 eggs and 2.45BGN left.


# INPUT:
# 15.75
# 1.4

# EXPECTED OUTPUT:
# You made 5 cozonacs! Now you have 14 eggs and 1.31BGN left.

budget = float(input())

flavour_per_Kg_price = float(input())
eggs_per_pack_price = 0.75 * flavour_per_Kg_price
milk_per_liter_price = flavour_per_Kg_price + flavour_per_Kg_price * 0.25

colored_eggs = 0
cozonacs = 0

recipe = eggs_per_pack_price + flavour_per_Kg_price + milk_per_liter_price / 4

while budget > 0:
    if budget - recipe < 0:
        break
    colored_eggs += 3
    cozonacs += 1
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2
    budget -= recipe

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
