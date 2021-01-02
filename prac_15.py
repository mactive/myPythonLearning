from sys import argv
script, filename = argv

for item in argv:
    print(item)

txt = open(filename)

print(f"Here's your filename {filename}.")
print(txt.read())

print("Type the filename again: ")

file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())

