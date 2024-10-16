def PrintBoxByWidth(width):
    for _ in range(width):
        print("x", end='')
    print("")
    
    print("x", end='')
    for _ in range(width - 2):
        print(" ", end='')
    print("x", end='')
    print("")

    print("x", end='')
    for _ in range(width - 2):
        print("o", end='')
    print("x", end='')
    print("")

    print("x", end='')
    for _ in range(width - 2):
        print(" ", end='')
    print("x", end='')
    print("")

    for _ in range(width):
        print("x", end='')
    print("")