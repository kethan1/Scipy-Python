import os

while True:
    print(f"pwd: {os.getcwd()}")
    for file in os.listdir("./"):
        print(f" - {file}")
    action = input("Do you want to 'delete' a file, 'create' a file, move to a new folder ('cd'), or quit('q')? ")
    action_split = action.split()
    if action_split[0] == "delete":
        os.remove(action_split[1])
    elif action_split[0] == "create":
        if not os.path.exists(action_split[1]):
            with open((action_split[1]), "w"):
                pass
    elif action_split[0] == "cd":
        os.chdir(action_split[1])
    elif action_split[0] == "q":
        break
