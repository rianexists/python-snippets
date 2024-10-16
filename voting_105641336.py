vote = {1:0, 2:0, 3:0}
abc = "ABC"
exit = False
format = """Electronic voting
1.  Vote A
2.  Vote B
3.  Vote C
4.  Print (current tally)
5.  Exit"""

while not exit:
    print(format)
    option = int(input())
    if option == 5:
        exit = True
    elif option == 4:
        print(F"Votes tally:\n  A:  {vote[1]}\n  B:  {vote[2]}\n  C:  {vote[3]}")
    else:
        vote[option] += 1