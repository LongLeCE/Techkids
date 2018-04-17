from turtle import *
shape("turtle")
speed(0)
for k in range(36):
    for i in range(2):
        j = 0
        z = 0
        while z < 90:
            j = j + 1
            forward(20 + j)
            right(1 + j)
            z = z + 1 + j
        forward(25)
        j = j + 1
        while z > 0:
            j = j - 1
            right(1 + j)
            forward(20 + j)
            z = z - 1 - j
    right(10)
n = input("")