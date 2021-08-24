square_meters = float(input())
cost_in_the_moment = square_meters * 7.61
discount = cost_in_the_moment * 0.18
final_cost = cost_in_the_moment - discount
print(f"The final price is: {final_cost} lv.")
print(f"The discount is: {discount} lv.")