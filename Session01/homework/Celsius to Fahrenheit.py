def isnumber(a):
    try:
        float(a)
    except ValueError:
        return False
    return True


print("This program is written to help you convert Celsius to Fahrenheit.")
while True:
    n = input("Enter temperature in Celsius: ")
    while (not isnumber(n)) or (float(n) < -273.15):
        if not isnumber(n):
            print("Please input numbers only!")
        else:
            if float(n) < -273.15:
                print("That's below Absolute zero! Please enter a higher temperature.")
        n = input("\nEnter temperature in Celsius: ")
    print(n, "(C) =%8.1f (F)" % (float(n) * 1.8 + 32))
    m = input("Do you want to convert again? (y/n): ")
    while (m != 'n') and (m != 'y'):
        print("Please input y for yes or n for no only!")
        m = input("\nDo you want to convert again? (y/n): ")
    if m == 'n':
        break