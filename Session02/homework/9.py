m = int(input("So hang: "))
n = int(input("So cot: "))
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(j*i)
    a.append(b)
print(a)
