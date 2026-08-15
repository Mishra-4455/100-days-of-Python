import random
import Hangman_stages
import Hangman_words

chosen_word = random.choice(Hangman_words.word_list)
display = ['_'] * len(chosen_word)
guesses = []
length = len(chosen_word)
lives = 6
flag = 0

print(Hangman_stages.logo)

while lives != 0:
    flag = 0
    print (Hangman_stages.stages[lives])
    guess = (input("Enter a letter: ")).lower()
    if guess not in guesses:
        guesses += guess
        for i in range(length):
            if(chosen_word[i] == guess):
                print (f"You have entered '{guess}', which is a correct guess")
                display[i] = guess
                flag += 1
        if flag == 0:
            print(f"You have entered '{guess}', which is a wrong guess")
            lives -= 1
        print(f"{' '.join(display)}")

        if lives == 0:
            print(Hangman_stages.stages[0])
            print("The word was", chosen_word)
            print("Try again ;)")
        if '_' not in display:
            print("You Win!")
            lives = 0
    else:
        print(f"You already guessed {guess}, you may go again")
        print(f"{' '.join(display)}")