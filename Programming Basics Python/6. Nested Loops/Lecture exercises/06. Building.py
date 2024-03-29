# Напишете програма, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред), като са изпълнени следните условия:
# ⦁	На всеки четен етаж има само офиси;
# ⦁	На всеки нечетен етаж има само апартаменти;
# ⦁	Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента},
# номерата на апартаментите започват от 0;
# ⦁	Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса},
# номерата на офисите също започват от 0;
# ⦁	На последният етаж винаги има апартаменти и те са по-големи от останалите,
# затова пред номера им пише 'L', вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

# input:
# 6
# 4
# expected output:
# L60 L61 L62 L63
# A50 A51 A52 A53
# O40 O41 O42 O43
# A30 A31 A32 A33
# O20 O21 O22 O23
# A10 A11 A12 A13

# input:
# 9
# 5
# expected output:
# L90 L91 L92 L93 L94
# O80 O81 O82 O83 O84
# A70 A71 A72 A73 A74
# O60 O61 O62 O63 O64
# A50 A51 A52 A53 A54
# O40 O41 O42 O43 O44
# A30 A31 A32 A33 A34
# O20 O21 O22 O23 O24
# A10 A11 A12 A13 A14

floors = int(input())
apartments = int(input())

for number in range(floors, 0, -1):
    for n in range(0, apartments):
        if number == floors:
            print(f"L{number}{n}", end=" ")
        elif number % 2 == 0:
            print(f"O{number}{n}", end=" ")
        else:
            print(f"A{number}{n}", end=" ")
    print()
