import random
number=random.randint(1,100)
print(number)
while True:
    guess=int(input("Guess a number between 1 and 100: "))
    if guess>number:
        print("Too High")
    elif guess<number:
        print("Too Low")
    else:
        print("your guess is correct")
        break