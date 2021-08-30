# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип
# от продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.

# Вход
# Входът е поредица от цели числа и текст:
# ⦁	На първия ред до получаване на командата "Finish" - име на филма – текст
# ⦁	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# ⦁	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаванe
# на командата "End":
# ⦁	Типа на закупения билет - текст ("student", "standard", "kid")

# Изход
# На конзолата трябва да се печатат следните редове:
# ⦁	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# ⦁	При получаване на командата "Finish" да се отпечатат четири реда:
# ⦁	"Total tickets: {общият брой закупени билети за всички филми}"
# ⦁	"{процент на студентските билети}% student tickets."
# ⦁	"{процент на стандартните билети}% standard tickets."
# ⦁	"{процент на детските билети}% kids tickets."


# input:
# Taxi
# 10
# standard
# kid
# student
# student
# standard
# standard
# End
# Scary Movie
# 6
# student
# student
# student
# student
# student
# student
# Finish
# expected output:
# Taxi - 60.00% full.
# Scary Movie - 100.00% full.
# Total tickets: 12
# 66.67% student tickets.
# 25.00% standard tickets.
# 8.33% kids tickets.

# input:
# The Matrix
# 20
# student
# standard
# kid
# kid
# student
# student
# standard
# student
# End
# The Green Mile
# 17
# student
# standard
# standard
# student
# standard
# student
# End
# Amadeus
# 3
# standard
# standard
# standard
# Finish
# expected output:
# The Matrix - 40.00% full.
# The Green Mile - 35.29% full.
# Amadeus - 100.00% full.
# Total tickets: 17
# 41.18% student tickets.
# 47.06% standard tickets.
# 11.76% kids tickets.

command_film = input()

ticket_standard = 0
ticket_student = 0
ticket_kid = 0
sum_tickets = 0
counter_tickets = 0

while command_film != "Finish":
    free_places = int(input())

    ticket = input()
    while ticket != "End":
        counter_tickets += 1
        if ticket == "standard":
            ticket_standard += 1
        elif ticket == "kid":
            ticket_kid += 1
        elif ticket == "student":
            ticket_student += 1
        if counter_tickets == free_places:
            over = True
            break
        ticket = input()

    print(f"{command_film} - {(counter_tickets / free_places)*100:.2f}% full.")
    sum_tickets += counter_tickets
    counter_tickets = 0

    command_film = input()
print(f"Total tickets: {sum_tickets}")
print(f"{(ticket_student/sum_tickets)*100:.2f}% student tickets.")
print(f"{(ticket_standard/sum_tickets)*100:.2f}% standard tickets.")
print(f"{(ticket_kid/sum_tickets)*100:.2f}% kids tickets.")
