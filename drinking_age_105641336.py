age = int(input("What is your year of birth: "))

print("You are " + str((2024 - age)) + " years old")
print("Come in and have a drink!" if age <= 2006 else "Go away. Child.")