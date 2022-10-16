import random

random_number = random.randint(1, 100)
guess = int(input("guess a number\n"))
while random_number != guess:
    guess = int(input("guess a number \n"))
    if guess > random_number:
        print("please select a smaller number")
    if guess < random_number:
        print("please select a greater number")
    if guess == random_number:
        print("you guessed the correct number")
        print("thanks for playing our game")
        rate = int(input("please rate our game out of 5 star\n"))
        if rate < 4:
            print(f"YOU RATED {rate} star,sorry for any inconviness,by time our technical team will improve the game.")
            print("Thanks for rating the game it will help us a lot.")
        if rate >= 4:
            print(f"YOU RATED {rate} star,thanks for good rating , your rating gives us motivation to develop more games.")
exit()