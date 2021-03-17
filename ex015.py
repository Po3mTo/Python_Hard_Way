from sys import argv
#script = ex015.py filename = ex015_sample.txt
script, filename = argv
# new variable and command to open
txt = open(filename)
# common print
print(f"Here's your file {filename}:")
# NEW!!! We've got our variable "txt" + .read() to read the file.
print(txt.read())
# Again common print
print("Type the filename again:")
# We give a file name which we want to open. In this case it's ex015_sample.txt
file_again = input("- ")
# we name our operation txt_again
txt_again = open(file_again)
# We have the same thing as before on 9 line. We print txt_again(it opens our file) + .read to read our file and show us what's inside.
print(txt_again.read())
