# Create a program that creates a file called my_first_file.txt. In that file write a single line with the content: 'I just created my first file!'

file_path = "my_first_file.txt"
content = "I just created my first file"

with open(file_path, "w") as file:
    file.write(content)
