def shopping_list(budget_number: int, **kwargs):
    basket = 0
    list_with_messages = []
    if budget_number >= 100:
        for name, value in kwargs.items():
            price, quantity = value
            all_sum_for_product = price * quantity

            if budget_number >= all_sum_for_product:
                budget_number -= all_sum_for_product
                basket += 1
                list_with_messages.append(f"You bought {name} for {all_sum_for_product:.2f} leva.")
            if basket == 5:
                return ('\n').join(list_with_messages)
        return ('\n').join(list_with_messages)
    else:
        return "You do not have enough budget."


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))