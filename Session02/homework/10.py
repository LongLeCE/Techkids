x = [int(y,2) for y in input("Nhap day: ").split(',')]
for i in x:
    if i % 5 == 0:
        print(format(i, 'b'), end=",")
print("\b")
