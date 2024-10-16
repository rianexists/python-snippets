values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]

sum, max = [0, 0]

i = 0
while i < len(values):
    if values[i] > max:
        max = values[i]
    sum += values[i]
    i += 1
#for value in values:
#    if value > max:
#        max = value
#    sum += value

average = sum / len(values)
print(f"""{'Sum: ':10}{sum:15}
{'Average: ':10}{average:15}
{'Max: ':10}{max:15}""")