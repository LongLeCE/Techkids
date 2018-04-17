for i in range(0, 51):
    if i % 3 == 0:
        if i % 5 == 0:
            print("Fizz", end="")
        else:
            print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    elif i % 3 != 0:
        print(i)
