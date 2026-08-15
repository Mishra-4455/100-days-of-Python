''' #1 create a empty list called display. For every letter in the chosen_word there should be a '_' in display
    #2 loop through each of the letters in the chosen_word, if a word 'guess' matches any index in the chosen_word then
    replece the '_' with guess
    #3 print guess'''


import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
done = False

print(chosen_word)
while not done:
    guess = (input("Enter a letter: ")).lower()
    for i in range(len(chosen_word)):
        if(chosen_word[i] == guess):
            display[i] = guess
    print(display)

    if '_' not in display:
        print("You Win!")
        done = True