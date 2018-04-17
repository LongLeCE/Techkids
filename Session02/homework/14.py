a = 0
for i in range(9):
    a = a + 1
    for j in range(i+1):
        if j < i:
            print(a, end="")
        else:
            print(a)
