name = input("What is your name: ")

words = name.split(" ")
initials = ""
for word in words:
    initials += word[0].upper()
print(initials)