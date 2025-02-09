#checkerboard

s = str(input("Enter a string for design: "))

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print(" ", end="")
        else:
            print(s, end="")
    else:
        print(s)