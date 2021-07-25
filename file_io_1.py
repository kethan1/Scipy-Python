# with open(input("What file do you want me to open and close?\n"), "w") as file:
#     pass

# with open(input("File to read?\n"), "r") as file:
#     print(file.read())

with open(input("File to write?\n"), "w") as file:
    print(input("What do you want to write to the file?\n"), file=file)
