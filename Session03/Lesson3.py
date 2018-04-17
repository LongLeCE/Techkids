# [1]
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end = ",")
# print("\b")

# [2]
# z = 1
# for i in range(1, int(input("Nhap so: "))):
#     z *= (i+1)
# print("Ket qua:", z)

# [3]
# d = {i+1: (i+1)**2 for i in range(int(input("Input: ")))}
# print(d)

# [4]
# a = [i for i in input("Input: ").split(",")]
# print(a)
# print(tuple(a))

# [5]
# print(chr(int(input("Nhap ma ASCII: "))).encode('utf-8'))

# [6]
# # -*- coding: utf-8 -*-

# [7]
# a = 0
# for i in range(int(input("Input: "))):
#     a += (i+1)/(i+2)
# print("{0:.2f}".format(a))

# [8]
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# [9]
# if int(input("Nhap so: ")) % 2 == 0:
#     print("So chan")
# else:
#     print("So le")

# [10]
# print(1+100*int(input("Input: ")))

# [11]
# a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# b = [a[0]]
# for i in range(len(a)):
#     k = 0
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             k = 1
#             break
#     if k == 0:
#         b.append(a[i])
# print(b)

# [12]
# for i in range(1, 35):
#     if 2*i+4*(35-i) == 94:
#         print("So ga:", i, "\nSo tho:", 35-i)
#         break

a = (1, 2, 3)
b = (1, 2)
print(hex(id(a)))
a = a + b
print(a)
print(hex(id(a)))
c = [1, 2, 3]
print(hex(id(c)))
c.append([1, 2])
print(c)
print(hex(id(c)))
