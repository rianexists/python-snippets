names = ["frank", "george"]
entry = input("Enter your name: ").lower()
print("Welcome " + entry if entry in names else "Go away")