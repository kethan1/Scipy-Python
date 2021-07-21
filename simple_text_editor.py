import sys
import os

if sys.argv[1:]:
    filename = sys.argv[1]
else:
    filename = input("What file would you like to edit? ")

if not os.path.exists(filename):
    print("The file could not be found, creating it!")
    with open(filename, 'w'):
        pass

file = open(filename, "a+")
while True:
    print("Current contents in file:")
    file.seek(0)
    print(file.read())
    print()

    action = input("What action would you like to perform on the file, append text (a), save file (s), quit(q)? ")
    if action == "a":
        print(input("What text would you like to add: "), file=file)
        print("The text has been added")
        file.close()
        file = open(filename, "a+")
    elif action == "s":
        file.close()
        file = open(filename, "a+")
    elif action == "q":
        print("Saving File and Quitting...")
        break
    else:
        print("Invalid Option")
file.close()
