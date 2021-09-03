# Most football fans love it for the goals and excitement.
# Well, this problem does not.
# You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee
# , and the team with less than 7 players loses.
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g.
# the card 'B-7' means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space.
# You should print the count of remaining players on each team at the end of the game in the format:
# "Team A - {players_count}; Team B - {players_count}".
# If the game was terminated by the referee, print an additional line: "Game was terminated".
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.

# INPUT:
# A-1 A-5 A-10 B-2

# EXPECTED OUTPUT:
# Team A - 8; Team B - 10


# INPUT:
# A-1 A-5 A-10 B-2 A-10 A-7 A-3

# EXPECTED OUTPUT:
# Team A - 6; Team B - 10
# Game was terminated


A = []
B = []
is_terminated = False
for footballers in range(1, 12):
    A.append(footballers)
    B.append(footballers)

referee = input()
referee_list = referee.split(" ")

for n in range(0, len(referee_list)):
    if len(A) < 7:
        is_terminated = True
        break
    elif len(B) < 7:
        is_terminated = True
        break

    if referee_list[n][0] == "A":
        if len(referee_list[n]) > 3:
            number = referee_list[n][2] + referee_list[n][3]
            value = int(number)
            if value in A:
                A.remove(value)
        else:
            value = int(referee_list[n][2])
            if value in A:
                A.remove(value)
    else:
        if len(referee_list[n]) > 3:
            number = referee_list[n][2] + referee_list[n][3]
            value = int(number)
            if value in B:
                B.remove(value)
        else:
            value = int(referee_list[n][2])
            if value in B:
                B.remove(value)

print(f"Team A - {len(A)}; Team B - {len(B)}")
if is_terminated:
    print("Game was terminated")
