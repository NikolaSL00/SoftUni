# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее
# да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.

# Вход
# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.

# Изход
# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."

# input:
# 2000
# 1000
# spend
# 1200
# save
# 2000
# expected output:
# You saved the money for 2 days.

# input:
# 110
# 60
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10
# expected output:
# You can't save the money.
# 5

needed_money = float(input())
money = float(input())

type_action = ""
sum_action = 0

counter_spending = 0
days_counter = 0

while needed_money > money:
    type_action = input()
    sum_action = float(input())
    days_counter += 1
    if type_action == "spend":
        if money < sum_action:
            money = 0
        else:
            money -= sum_action
        counter_spending += 1
    else:
        counter_spending = 0
        money += sum_action
    if counter_spending == 5:
        print(f"You can't save the money.")
        print(f"{days_counter}")
        break
else:
    print(f"You saved the money for {days_counter} days.")
