# Write the function between the START and END tags
# START

def add_two_numbers(a, b):
    return a + b

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(add_two_numbers(1, 2) == 3))
print("Test 2 Passed: " + str(add_two_numbers(5, 6) == 11))
print("Test 3 Passed: " + str(add_two_numbers(9, 0) != 10))