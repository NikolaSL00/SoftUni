# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return the list of to-do notes sorted by importance.
# The importance value will always be an integer between 1 and 10 (inclusive).

# INPUT:
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

# EXPECTED OUTPUT:
# ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']


new_note = input()
to_do_notes = [0] * 10

while not new_note == "End":
    importance, activity = new_note.split("-")
    importance = int(importance)
    importance -= 1
    to_do_notes.pop(importance)
    to_do_notes.insert(importance, activity)

    new_note = input()

result = [el for el in to_do_notes if not el == 0]
print(result)
