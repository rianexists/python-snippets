arr1 = [8, 2, 17, 11]
arr2 = arr1
print("arr2:",arr2)

arr1[2] = 999

print("arr1:",arr1)
print("arr2:",arr2)

arr3 = arr1.copy()
print("arr3:",arr3)
arr3[0] = -7
print("arr1:",arr1)
print("arr3:",arr3)