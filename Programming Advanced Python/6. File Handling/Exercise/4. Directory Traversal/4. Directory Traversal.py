# Write a program that traverses a given directory for all files. Search through the first level of the directory only and write information about each found file in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should be saved on the Desktop. Ensure the desktop path is always valid, regardless of the user.

import os


def traverse_directories(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(file_with_path):
            ext = x.split(".")[-1]
            if ext not in result:
                result[ext] = []
            result[ext].append(file_with_path)
        elif os.path.isdir(file_with_path):
            traverse_directories(file_with_path, result)


result = {}
traverse_directories(os.getcwd(), result)

with open("output.txt", "w") as result_file:
    for ext, files in sorted(result.items()):
        result_file.write(f".{ext}")
        result_file.write("\n")
        for file in files:
            result_file.write(f"---{file}")
            result_file.write("\n")
