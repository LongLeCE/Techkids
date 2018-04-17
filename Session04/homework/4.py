a = [(1, 2, 40), (0, 15, 60), (10, 80, 0)]
for i in range(len(a)):
    a[i] = [j for j in a[i]]
    a[i][2] = 100
    a[i] = tuple(a[i])
print(a)
