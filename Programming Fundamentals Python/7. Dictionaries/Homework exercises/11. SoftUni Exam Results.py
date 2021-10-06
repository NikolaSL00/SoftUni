# Judge statistics on the last Programing Fundamentals exam was not working correctly, so you have the task to take all the submissions and analyze them properly. You should collect all the submissions and print the final results and statistics about each language that the participants submitted their solutions in.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and his submissions and points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest, but preserve his submissions in the total count of submissions for each language.
# After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:
# Results:
# {username} | {points}
# …
# After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:
# Submissions:
# {language} - {submissionsCount}
# …
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}".
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# Print the exam results for each participant, ordered descending by max points and then by username, in the following format:
# Results:
# {username} | {points}
# …
# After that print each language, ordered descending by total submissions and then by language name, in the following format:
# Submissions:
# {language} - {submissionsCount}
# …
# Allowed working time / memory: 100ms / 16MB.

# INPUT:
# Pesho-Java-84
# Gosho-C#-84
# Gosho-C#-70
# Kiro-C#-94
# exam finished

# OUTPUT:
# Results:
# Kiro | 94
# Gosho | 84
# Pesho | 84
# Submissions:
# C# - 3
# Java - 1

# INPUT:
# Pesho-Java-91
# Gosho-C#-84
# Kiro-Java-90
# Kiro-C#-50
# Kiro-banned
# exam finished

# OUTPUT:
# Results:
# Pesho | 91
# Gosho | 84
# Submissions:
# C# - 2
# Java - 2

input_line = input()

result_dictionary = {}
submission_dict = {}

while input_line != "exam finished":
    #    participant, pr_language, points = input_line.split("-")
    command_info = input_line.split("-")

    if command_info[1] != "banned":
        st_name = command_info[0]
        subject = command_info[1]
        points = int(command_info[2])
        if subject not in result_dictionary.keys():
            result_dictionary[subject] = dict()
            submission_dict[subject] = 0
            result_dictionary[subject][st_name] = points
            submission_dict[subject] += 1

        elif st_name in result_dictionary[subject]:
            submission_dict[subject] += 1
            if result_dictionary[subject][st_name] < points:
                result_dictionary[subject][st_name] = points
        else:
            result_dictionary[subject][st_name] = points
            submission_dict[subject] += 1

    else:
        for command_info[1], students_with_points in result_dictionary.items():
            if command_info[0] in students_with_points.keys():
                students_with_points.pop(command_info[0])

    input_line = input()


def dict_to_List(dictionary: dict, result_list: list):
    for subject, st_name_and_points in dictionary.items():
        for st_name, points in st_name_and_points.items():
            if st_name != "banned":
                result_list.append([st_name, points])


result_list = []
dict_to_List(result_dictionary, result_list)

print("Results:")
for el in sorted(result_list, key=lambda x: (-x[1], x[0])):
    print(f"{el[0]} | {el[1]}")

print("Submissions:")
for subject, count in sorted(submission_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{subject} - {count}")
