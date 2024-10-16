from datetime import datetime

year = datetime.now().year

print("Born: " + str(year - int(input("Enter age: "))))