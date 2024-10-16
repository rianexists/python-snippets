## Rian Webster
## 105641336
## 06/08/2024
import random

print("Greetings! What is your name?")
name = input()
print("And your Student ID please.")
id = input()

print("Nice to meet you", name)
print("Your Student ID is noted as", id)

rand = random.randrange(1,len(id)-3)
total = int(id[rand])
total += int(id[rand+1])
total += int(id[rand+2])
total += int(id[rand+3])
print(total)