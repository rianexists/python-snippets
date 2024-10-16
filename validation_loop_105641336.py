while True:
    rate = int(input("Enter pay rate: "))
    hours = int(input("Enter hours: "))

    if rate >= 23 and 1 <= hours <= 20:
        print(f"Total: {rate * hours}")
    else:
        print("Entry rejected: invalid data")

    if input('Continue ("Y" for yes): ') != "Y":
        print("Goodbye!")
        break