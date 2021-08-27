# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

# input:
# 1
# 46
# expected output:
# 2:01

# input:
# 0
# 01
# expected output:
# 0:16

# input:
# 23
# 59
# expected output:
# 0:14

hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes
total_minutes += 15

hours = total_minutes // 60
minutes = total_minutes % 60

hour_system = hours % 24
if minutes < 10:
    print(f"{hour_system}:0{minutes}")
else:
    print(f"{hour_system}:{minutes}")