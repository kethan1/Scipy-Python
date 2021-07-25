import os

if os.path.exists(input("File name to check? ")):
    print("File exists")
else:
    print("File could not be found")

for index, item in enumerate(os.listdir(os.path.expanduser(input("Folder to list? ")))):
    print(f"{index}) {item}")

with open("test.txt", "r+") as file:
    file.seek(5)
    print(file.read())
    file.seek(5)
    file.write("!")

os.remove(input("File to remove: "))

with open(input("File to create: "), "w"):
    pass
