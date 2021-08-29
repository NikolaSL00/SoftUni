# ⦁	Ани отива до родния си град след много дълъг период извън страната.
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст).
# Книгите в библиотеката са свършили щом получите текст “No More Books”.Ако не открие търсената книгата,
# да се отпечата на два реда:

# ⦁	"The book you search is not here!"
# ⦁	"You checked {брой} books."
# ⦁	Ако открие книгата си, да се отпечата на един ред:
# ⦁	"You checked {брой} books and found it."

# input:
# Troy
# Stronger
# Life Style
# Troy
# expected output:
# You checked 2 books and found it.

# input:
# The Spot
# Hunger Games
# Harry Potter
# Torronto
# Spotify
# No More Books
# expected output:
# The book you search is not here!
# You checked 4 books.

searched_book = input()
next_book = input()
iterations = 0
while searched_book != next_book:
    if next_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {iterations} books.")
        break
    next_book = input()
    iterations += 1
else:
    print(f"You checked {iterations} books and found it.")
