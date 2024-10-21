from random import randrange

secret_number = randrange(11)

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = 0
while number != secret_number:
    number = int(input())
    if number == secret_number:
        break
    print("Ha ha! You're stuck in my loop!")
    print("Your guess was too", "high" if number > secret_number else "low")

print("Well done, muggle! You are free now.")