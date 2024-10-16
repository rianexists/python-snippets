gates = [1, 2, 4, 8]
total = 0

print("Welcome. Please enter Y or N as to whether the gate is open")
for i, gate in enumerate(gates):
    if input(f"Gate {i+1} open (Y/N): ") == "Y":
        total += gate

print(f"Code: {total}")