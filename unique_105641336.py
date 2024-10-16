number = input("Enter a number: ")

previous = []
repeating = []
while number != "x":
    number = int(number)
    if number in previous:
        repeating.append(number)
    previous.append(number)
    number = input("Enter a number: ")
print("Repeating numbers:", repeating)