# Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times, print the message: 'File already deleted!'.

import os
from os import path

if path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")
