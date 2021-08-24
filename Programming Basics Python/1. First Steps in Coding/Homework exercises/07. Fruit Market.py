# Мария решава да мине на диета и отива до  близкия пазар, за да купи ягоди,
# банани, портокали и малини. Да се напише програма, която пресмята колко пари са
# ѝ необходими за да плати сметката, като знаете, че:
# ⦁	цената на  малините е на половина по-ниска от тази на ягодите;
# ⦁	цената на портокалите е с 40% по-ниска от цената на малините;
# ⦁	цената на бананите е с 80% по-ниска от цената на малините.

# От конзолата се четат 5 реда:
# ⦁	Цена на ягодите в лева – реално число;
# ⦁	Количество на бананите в килограми – реално число;
# ⦁	Количество на портокалите в килограми – реално число;
# ⦁	Количество на малините в килограми – реално число;
# ⦁	Количество на ягодите в килограми – реално число.

# input ->    57.5
#             10
#              3.4
#              6.5
#              1.7
# expected output ->  400.775

# input ->    63.5
#              3.57
#              6.35
#              8.15
#              2.5
# expected output ->  561.1495

berries_price = float(input())
raspberries_price = berries_price / 2
bananas_price = float(input()) * (raspberries_price - raspberries_price * 0.8)
orange_price = float(input()) * (raspberries_price - raspberries_price * 0.4)
raspberries_need = float(input()) * (berries_price / 2)
berries = float(input())
berrries_need = berries_price * berries

sum = berrries_need + bananas_price + orange_price + raspberries_need
print(sum)
