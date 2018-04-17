s = input("Password: ")
a = b = c = d = 0
if 6 <= len(s) <= 16:
    for i in s:
        if a == 0:
            if i.islower():
                a = 1
        if b == 0:
            if i.isupper():
                b = 1
        if c == 0:
            if i.isdigit():
                c = 1
        if d == 0:
            if not i.isalnum():
                d = 1
        if a == b == c == d == 1:
            print("Password is valid")
            break
if a == 0 or b == 0 or c == 0 or d == 0:
    print("Invalid password!")
