from collections import deque

dictionary_with_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}


def decide_what_to_craft(res: int):
    if 100 <= res <= 199:
        dictionary_with_gifts["Gemstone"] += 1
    elif 200 <= res <= 299:
        dictionary_with_gifts["Porcelain Sculpture"] += 1
    elif 300 <= res <= 399:
        dictionary_with_gifts["Gold"] += 1
    elif 400 <= res <= 499:
        dictionary_with_gifts["Diamond Jewellery"] += 1


def sum_materials(last_material, first_magic):
    sum_of_both = last_material + first_magic

    if sum_of_both < 100:

        if sum_of_both % 2 == 0:
            last_material *= 2
            first_magic *= 3
            decide_what_to_craft(last_material + first_magic)
        else:
            last_material *= 2
            first_magic *= 2
            decide_what_to_craft(last_material + first_magic)

    elif sum_of_both > 499:
        sum_of_both /= 2
        decide_what_to_craft(sum_of_both)

    else:
        decide_what_to_craft(sum_of_both)


materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

succeed_flag = False

while materials and magic_levels:
    last_material = materials.pop()
    first_magic = magic_levels.popleft()

    sum_materials(last_material, first_magic)

    if (dictionary_with_gifts["Gemstone"] >= 1 and dictionary_with_gifts["Porcelain Sculpture"] >= 1) or (
            dictionary_with_gifts["Gold"] >= 1 and dictionary_with_gifts["Diamond Jewellery"] >= 1):
        succeed_flag = True


a= 5
if succeed_flag:
    print("The wedding presents are made!")
    if materials:
        print(f"Materials left: {(', ').join([str(x) for x in materials])}")
    if magic_levels:
        print(f"Magic left: {(', ').join([str(x) for x in magic_levels])}")

    for key, value in sorted(dictionary_with_gifts.items()):
        if value >= 1:
            print(f"{key}: {value}")
else:
    print("Aladdin does not have enough wedding presents.")
    if materials:
        print(f"Materials left: {(', ').join([str(x) for x in materials])}")
    if magic_levels:
        print(f"Magic left: {(', ').join([str(x) for x in magic_levels])}")
    for key, value in sorted(dictionary_with_gifts.items()):
        if value >= 1:
            print(f"{key}: {value}")
