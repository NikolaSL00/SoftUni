# Напишете програма, която чете текст от конзолата(стринг) и го принтира,
# докато не получи командата "Stop".

# input:
# Nakov
# SoftUni
# Sofia
# Bulgaria
# SomeText
# Stop
# AfterStop
# Europe
# HelloWorld
# expected output:
# Nakov
# SoftUni
# Sofia
# Bulgaria
# SomeText

# input:
# Sofia
# Berlin
# Moscow
# Athens
# Madrid
# London
# Paris
# Stop
# expected output:
# Sofia
# Berlin
# Moscow
# Athens
# Madrid
# London
# Paris

word = input()

while word != "Stop":
    print(word)
    word = input()
