# Write a program that reads a text file and inserts line numbers in front of each of its lines and counts all the letters and punctuation marks. The result should be written to another text file.

punctuation_marks = {"-", ".", "?", "!", "'", ","}

count_of_lines = 0

with open("text.txt", "r") as file, open("output.txt","w") as result:
    for line in file:
        count_of_lines += 1
        count_of_punctuation_marks = 0
        count_of_letters = 0
        for el in line:
            if el in punctuation_marks:
                count_of_punctuation_marks += 1
            elif el.isalpha():
                count_of_letters += 1
        result.write(f"Line {count_of_lines}: {line.strip()} ({count_of_letters})({count_of_punctuation_marks})\n")
