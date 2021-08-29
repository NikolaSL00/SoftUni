# Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.
# За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
# Според сайта се налагат различни глоби:

# ⦁	"Facebook" -> 150 лв.
# ⦁	"Instagram" -> 100 лв.
# ⦁	"Reddit" -> 50 лв.

# От конзолата се четат два реда:
# ⦁	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# ⦁	Заплата - число в интервала [500...1500]

# След това n – на брой пъти се чете име на уебсайт – текст
# Ако по време на проверката заплатата стане по-малка или равна на 0 лева, на конзолата се изписва
# "You have lost your salary." и програмата приключва.
# В противен случай след проверката на конзолата се изписва остатъкът от заплатата.

# input:
# 10
# 750
# Facebook
# Dev.bg
# Instagram
# Facebook
# Reddit
# Facebook
# Facebook
# expected output:
# You have lost your salary.

# input:
# 3
# 500
# Github.com
# Stackoverflow.com
# softuni.bg
# expected output:
# 500

number_tabs = int(input())
salary = int(input())
restriction = 0
for i in range(0, number_tabs):
    name_website = input()
    if name_website == "Facebook":
        restriction += 150
    elif name_website == "Instagram":
        restriction += 100
    elif name_website == "Reddit":
        restriction += 50
salary = salary - restriction
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
