# Write the function between the START and END tags
# START

def FibonacciAdder(num):
    fib = [0, 1]
    total = 0
    while len(fib) < num:
        fib.append(fib[-2:-1][0] + fib[-1:][0])
    for item in fib:
        total += item
    return total

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))