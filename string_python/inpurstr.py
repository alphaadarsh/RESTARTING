username = input("Enter your username: ")

username.find(" ")  # this is used to find the index of the first occurrence of a space in the username. if there is no space in the username, it will return -1.

if len(username) > 15:
    print("Username must be no more than 15 characters long.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must contain only letters.")
else:
    print("Username is valid.")