a = b = 0
c = [int(x) for x in input("Nhap day so: ").split(',')]
for i in c:
    if i % 2 == 0:
        a += 1
    else:
        b += 1
print("So so chan:", a, "\nSo so le:", b)
