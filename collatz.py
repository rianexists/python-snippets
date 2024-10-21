def count(c0):
    if count == 0:
        raise SystemExit(0)
    print("Time to test the theory...")
    ##c0 = int(input())
    counter = 0

    while c0 != 1:
        counter += 1
        print(str(round(c0)))
        if c0 % 2 == 0:
            c0 /= 2
        else:
            c0 = (3 * c0) + 1

    print(1)
    print()
    print("Total steps: " + str(counter))

for i in range(1, 1000):
    count(i)