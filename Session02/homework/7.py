a = []
for i in range(2):
    a.append(1)
i = 1
while a[i] <= 50:
    i += 1
    a.insert(i+1, a[i-1] + a[i-2])
for i in range(0, len(a) - 1):
    print(a[i])
