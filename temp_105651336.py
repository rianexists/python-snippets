temp = int(input("What is the current temperature: "))

print("Freezing conditions" if temp <= 0 else "Cold conditions" if temp < 20 else "Mild weather" if temp < 30 else "Hot weather" if temp < 40 else "Extreme heat")