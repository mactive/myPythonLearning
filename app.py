# age = input("What is your age?")
# print("Your age is: ", age)

# i = 1
# while i <= 10:
#     print(i * '*')
#     i += 1


names = ["John", "Bob", "Apple", "Fab"]
print(names.count("tt"))
print(len(names))
print(names.index("Bob"))
# 干掉队尾
print(names.pop())
print(names)
names.append(names[0])

# 干掉队首
print(names.pop(0))
print(names)