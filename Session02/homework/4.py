import random
x = random.randint(1,9)
y = int(input("Guess my number? "))
while y != x:
    y = int(input("Bad guessing!\n\nGuess again? "))
print("Well guessed!")
