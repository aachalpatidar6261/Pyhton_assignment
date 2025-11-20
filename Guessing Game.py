from random import random, randint
random_num = randint(1,100)

while True:
    user_guess = int(input("Enter number : "))

    if random_num == user_guess:
        print("correct number is guessed.")
        break
    elif random_num > user_guess:
        print("too low")
    else:
        print("too high")