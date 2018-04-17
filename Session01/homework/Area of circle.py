import math


def isnumber(a):
    try:
        float(a)
    except ValueError:
        return False
    return True


print("This program is written to help you calculate the area of a circle with a given radius.")
while True:
    n = input("Radius? ")
    while (not isnumber(n)) or (float(n) < 1):
        print("That's not a circle's radius!\nPlease input positive real numbers only!")
        n = input("\nRadius? ")
    print("Area =%8.1f" % (math.pi * float(n) * float(n)))
    m = input("Do you want to calculate another circle's area? (y/n): ")
    while (m != 'n') and (m != 'y'):
        print("Please input y for yes or n for no only!")
        m = input("\nDo you want to calculate another circle's area? (y/n): ")
    if m == 'n':
        break