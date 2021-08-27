# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# ⦁	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# ⦁	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# ⦁	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# ⦁	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

# Изход
# На първия ред отпечатайте:
# ⦁	"Late", ако студентът пристига по-късно от часа на изпита;
# ⦁	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# ⦁	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.

# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# ⦁	"mm minutes before the start" за идване по-рано с по-малко от час;
# ⦁	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри,
# например "1:05”;
# ⦁	 "mm minutes after the start" за закъснение под час;
# ⦁	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри,
# например "1:03”.

# input:
# 9
# 30
# 9
# 50
# expected output:
# Late
# 20 minutes after the start

# input:
# 9
# 00
# 10
# 30
# expected output:
# Late
# 1:30 hours after the start

# input:
# 11
# 30
# 12
# 29
# expected output:
# Late
# 59 minutes after the start

hour = int(input())
minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = hour * 60 + minute
arrival_time = arrival_hour * 60 + arrival_minute
result_time = exam_time - arrival_time

late_time_hours = abs(result_time) // 60
late_time_minutes = abs(result_time) % 60

if 0 <= result_time <= 30:
    print("On time")
    if result_time != 0:
        print(f"{result_time} minutes before the start")
elif result_time > 30:
    print("Early")
    if result_time < 60:
        print(f"{result_time} minutes before the start")
    else:
        if late_time_minutes > 9:
            print(f"{late_time_hours}:{late_time_minutes} hours before the start")
        else:
            print(f"{late_time_hours}:0{late_time_minutes} hours before the start")
else:
    print("Late")
    if result_time > -60:
        print(f"{abs(result_time)} minutes after the start")
    else:
        if late_time_minutes > 9:
            print(f"{late_time_hours}:{late_time_minutes} hours after the start")
        else:
            print(f"{late_time_hours}:0{late_time_minutes} hours after the start")

