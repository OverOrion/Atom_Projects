while True:
    print ("Who are you?")
    name = input()
    if name != "Avalon":
        print ("Access denied, you are not the user.")
        continue
    print("Hello, jake. What is the pasword?")
    password = input()
    if password == "Never lose hope":
        break
print ("Access granted.")
