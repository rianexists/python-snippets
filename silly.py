f = open("silly_output.py", "w")
f.write('print("What number are you trying to check?")\n')
f.write("i = int(input())\n")
for i in range(1000):
    if i == 0:
        f.write("if i == 0:\n")
        f.write(" print('Number was ' + str(i))\n")
    else:
        f.write("elif i == " + str(i) + ":\n")
        f.write(' print("Number was " + str(i))\n')
f.write('else:\n')
f.write(' print("Sorry, this program does not yet support numbers that high")')
f.close()