import random

stages = ['''
 +---+
 |   |
 O   |
/|L  |
/ L  |
     |
========
''','''
 +---+
 |   |
 O   |
/|L  |
/    |
     |
========
''','''
 +---+
 |   |
 O   |
/|L  |
     |
     |
========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
========
''','''
 +---+
 |   |
     |
     |
     |
     |
========
''']

word_list = ["joy", "cleaning", "sisters", "laptop", "cards", "sleeping", "bookshelf", "programing", "coding", "homecoming", "happy"]
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
lives = 6
flag = 0

while lives != 0:
    flag = 0
    print (stages[lives])
    guess = (input("Enter a letter: ")).lower()
    for i in range(len(chosen_word)):
        if(chosen_word[i] == guess):
            display[i] = guess
            flag += 1
    if flag == 0:
        lives -= 1
    print(display)

    if lives == 0:
        print(stages[0])
        print("The word was", chosen_word)
        print("Try again ;)")
    if '_' not in display:
        print("You Win!")
        lives = 0