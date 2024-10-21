print("What was your income for the last finanicla year?")
income = float(input())

if income <= 85528:
    tax = (income * .18) - 556.02
else:
    tax = 14839 + ((income - 85528) * 0.32)

print("The tax total is " + str((round(tax) if tax >= 0 else 0)))