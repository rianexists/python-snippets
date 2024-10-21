values = [input(), input(),input()]
print(values[0])

def calc(value):
    value = float(value)
    return 3*value**3-2*value**2+3*value-1

for i in values:
    print(calc(i))