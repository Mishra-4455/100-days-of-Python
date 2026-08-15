''' #1 Randomly chose a word from the word_list and assign it to a variable called chosen_word
    #2 Ask the user to guess a letter and assign it to variable called guess. make the guess lowercase.
    #3 Check if the letter the user guessed is one of the letters in the chosen word
'''
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
flag = 0
print(chosen_word)
guess = (input("Enter a letter: ")).lower()

for i in range(len(chosen_word)):
    if(chosen_word[i] == guess):
        print(f"Character is present at {i} index of the chosen word")
        flag += 1
if flag == 0:
    print("Not present in chosen word")