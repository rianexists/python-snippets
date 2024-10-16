people = [
    ['Mary Anne', 5],
    ['Bob', 20],
    ['Sue', 36],
    ['Tom', 228]
]
print(f"{'Name':15}{'Age':>4}")
for person in people:
    print(f"{person[0]:15}{person[1]:4}")