# [6]
# m = int(input("So hang: "))
# n = int(input("So cot: "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         b.append(j*i)
#     a.append(b)
# print(a)

# [6]
# a = [int(x) for x in input("Row, Column: ").split(",")]
# print([[i*j for i in range(a[1])] for j in range(a[0])])

# [7]
# for i in sorted(x for x in input("Input: ").split(",")):
#     print(i, end = ",")
# print("\b")

# a = [x for x in input("Input: ").split(",")]
# b = []
# while len(a) > 0:
#     z = a[0]
#     for i in range(1, len(a)):
#         if z >= a[i]:
#             z = a[i]
#     a.remove(z)
#     b.append(z)
# for x in b:
#     print(x, end=",")
# print("\b")

# [8]
# print(input("Input: ").upper())

# [9]
# s = input("Input: ")
# print("LETTERS", len("".join(x for x in s if x.isalpha())))
# print("DIGITS", len("".join(x for x in s if x.isdigit())))

# [10]
# s = input("Input: ")
# print("UPPER CASE", len("".join(x for x in s if x.isupper())))
# print("LOWER CASE", len("".join(x for x in s if x.islower())))

# [11]
# import operator
# a = [tuple(x.split(",")) for x in input("Input: ").split(";")]
# a.sort(key=operator.itemgetter(0, 1, 2))
# print(a)

# a = [tuple(x.split(",")) for x in input("Input: ").split(";")]
# b = []
# while len(a) > 0:
#     z = a[0]
#     for i in range(1, len(a)):
#         if z >= a[i]:
#             z = a[i]
#     a.remove(z)
#     b.append(z)
# print(b)

# [14]
# a = b = c = 1
# n = int(input("Input: "))
# for i in range(n-2):
#     b = c
#     c = a + b
#     a = b
# print(c)

#
# def fibonacci(x):
#     if x <=1:
#         return x
#     else:
#         return fibonacci(x-1)+fibonacci(x-2)
#
#
# print(fibonacci(int(input("Input: "))))

# [15]
# for s in ["I", "You"]:
#     for v in ["Play", "Love"]:
#         for o in ["Hockey", "Football"]:
#             print(s, v, o)

# [16]
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

# a = [tuple(x.split(",")) for x in input("Input: ").split(";")]
# b = []
# while len(a) > 0:
#     x = a[0]
#     y = x[0]
#     for i in range(len(a)):
#         if y >= a[i][0]:
#             y = a[i][0]
#             x = a[i]
#     b.append(x)
#     a.remove(x)
# while len(b) > 0:
#     x = b[0]
#     y = x[0]
#     for i in range(len(b)):
#         if y == b[i][0]:
#             if y >= b[i][1]:
#                 y = b[i][1]
#                 x = b[i]
#                 a.append(x)
#                 b.remove(x)
#         else:
#             a.append(b[i])
#             del(b[i])
# while len(a) > 0:
#     x = b[0]
#     y = x[0]
#     for i in range(len(a)):
#         if y == b[i][1]:
#             if y >= b[i][2]:
#                 y = b[i][2]
#                 x = b[i]
#                 b.append(x)
#                 a.remove(x)
#         else:
#             b.append(a[i])
#             del(a[i])
# print(b)


#     Thuoc tinh: variables
#     Phuong thuc: ham con
# Example:
class Hcn:
    width = 10
    height = 100

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def chuvi(self):
        # self: Ham chuvi() chi dung trong class Hcn
        c = (self.height+self.width)*2
        return c


# Tao
a1 = Hcn(10, 100)
a2 = Hcn(30, 100)
print("Chu vi a1:", a1.chuvi())
print("Chu vi a2:", a2.chuvi())
