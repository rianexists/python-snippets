pi2 = 3.141592654

i = 0
length = len(str(pi2))
while i < length - 1:
    #print(f"{pi2:{length}.{i}f}")
    #print("%*.*f" % (length,i,pi2))
    print("{2:{0}.{1}f}".format(length,i,pi2))
    i += 1
    