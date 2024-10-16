code = input("Enter 4 digit code: ")

if len(code) == 4 and code.isnumeric():
    print("Valid")
else:
    print("Invalid")