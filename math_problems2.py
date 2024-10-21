values = [input(),input(),input(),input(),input()]

def calc(x):
    x = int(x)
    return 1/(x+1/(x+1/(x+1/(x+(1/x)))))

for i in values:
    print(calc(i))