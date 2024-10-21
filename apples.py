apples = {"john":3,"mary":5,"adam":6}
total_apples = 0
for i in apples.keys():
    print(i + " had " + str(apples[i]) + " apples")
    total_apples += apples[i]
print("All together there were " + str(total_apples) + " apples")