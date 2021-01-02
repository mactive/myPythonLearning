from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbyg!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

print("And finally, we close it.")

finalfile = open(filename, mode='r')
print(finalfile.read())