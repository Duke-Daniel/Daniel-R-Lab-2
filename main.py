import random


game_number = random.randint(1,10)
print(game_number)
while(True):
    guess = int(input("guess a number between 1 and 10:"))
    if guess > game_number:
        print("To high")
    elif guess < game_number:
        print("To low")
    else:
        print("You Win")
        break