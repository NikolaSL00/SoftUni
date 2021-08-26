# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели, иска да отиде на екскурзия. Да се напише програма,
# която пресмята печалбата от поръчката.
# Цени на играчките:
# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# От конзолата се четат 6 реда:
# ⦁	Цена на екскурзията - реално число;
# ⦁	Брой пъзели - цяло число;
# ⦁	Брой говорещи кукли - цяло число;
# ⦁	Брой плюшени мечета - цяло число;
# ⦁	Брой миньони - цяло число;
# ⦁	Брой камиончета - цяло число.

# input:
# 40.8
# 20
# 25
# 30
# 50
# 10
# expected output:
# Yes! 418.20 lv left.

# input:
# 320
# 8
# 2
# 5
# 5
# 1
# expected output:
# Not enough money! 238.73 lv needed.

holiday_price = float(input())
number_puzzles = int(input())
number_speeking_dolls = int(input())
number_bear = int(input())
number_minions = float(input())
number_trucks = int(input())

sum = number_puzzles * 2.60 + number_speeking_dolls * 3 + number_bear * 4.10 + number_minions * 8.20 + number_trucks * 2

count_sum = number_bear + number_trucks + number_minions + number_puzzles + number_speeking_dolls

if count_sum >= 50:
    sum = sum - sum * 0.25

sum = sum - sum * 0.10

if sum >= holiday_price:
    print(f"Yes! {sum - holiday_price:.2f} lv left.")
else:
    print(f"Not enough money! {holiday_price - sum:.2f} lv needed.")
