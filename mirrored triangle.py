print("half pyramid pattern of stars *")
n = int(input("enter the number of rows u want: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()