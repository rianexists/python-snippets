print("Please enter your numbers. When you are done, please enter 'done'")
finished = False
my_list = []

while not finished:
    var = input()
    if var != "done":
        my_list.append(var)
    else:
        finished = True

new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print("The list with unique elements only:")
new_list.sort()
print(new_list)