import random


game_number = random.randint(1,10)
#print(game_number)
guess_count = 0

while(True):
    guess = int(input("guess a number between 1 and 10:"))
    guess_count += 1
    if guess > game_number:
        print("To high")
    elif guess < game_number:
        print("To low")
    else:
        print(f"You Win! It took you {guess_count} guesses.")
        if (guess_count) <= 3:
            print("Great guessing!")
        else:
            print("Try to guess the number in fewer attempts next time.")
        break
    