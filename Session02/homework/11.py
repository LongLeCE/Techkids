s = input("Input: ")
print("Letters", len("".join([letter for letter in s if letter.isalpha()])))
print("Digits", len("".join([letter for letter in s if letter.isdigit()])))
