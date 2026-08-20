import art
import random

print(art.logo)
print("Welcome to Guess the Number!!")
print("I am thinking of a number between 1 to 100.")
thinking = random.randint(1,101)
if input("Choose a difficulty. Type 'easy' or 'hard':\n") == 'easy':
    lives = 10
else:
    lives = 5

def game_over():
    if lives == 0:
        print("You've ran out of guesses, you lose.")
        return True
    else:
        return False

def guess_number():
    global lives
    print(f"You have {lives} attempts ramaining to guess the number.")
    guess = int(input("Make a guess:"))
    if guess == thinking:
        print(f"You got it! The number was {thinking}.")
    if guess > thinking:
        print("Too high.")
        lives -= 1
        if game_over():return
        print("Guess again.")
        guess_number()
    if guess < thinking:
        print("Too low.")
        lives -= 1
        if game_over():return
        print("Guess again.")
        guess_number()

guess_number()