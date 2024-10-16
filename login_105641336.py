users = {"bob":"password1234", "sally":"happy22phoebe"}

authenticated = False
while authenticated == False:
    print("-"*37)
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user in users and password == users[user]:
        authenticated = True
        print("Access Granted!")
        print("-"*37)
    else:
        print("Access Denied!")