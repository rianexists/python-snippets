number = input("Enter a number: ")
numbers = []
while number != "x":
    numbers.append(int(number))
    number = input("Enter a number: ")
print(numbers)