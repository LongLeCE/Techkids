def selection_sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            z = a[i]
            if a[i] <= a[j]:
                a[i] = a[j]
                a[j] = z
    return a


print(selection_sort([4, 8, 1, 3, 2, 9, 5, 7, 6]))
