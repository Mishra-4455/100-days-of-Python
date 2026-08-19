import BlackJack_art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play blackJack? 'y' for yes and 'n' for no.\n")
if play == 'y':
    print(BlackJack_art.logo)
    player = []
    computer = []
    score_p = 0
    score_c = 0
    for n in range(2):
        rand_card = random.choice(cards)
        player.append(rand_card)
        score_p += rand_card
        rand_card = random.choice(cards)
        computer.append(rand_card)
        score_c += rand_card
    print(f"    Your cards: {player}, your current score: {score_p}")
    print(f"    Computer's first card: {computer[0]}")
    if score_p == 21:
        print("BLACKJACK!!!!")
        print("You win!")
    elif score_c == 21:
        print("OPPONENT HAS A BLACKJACK!!!")
        print("Computer wins!\nyou lose!")
    else:
        while score_c <= 16:
            rand_card = random.choice(cards)
            computer.append(rand_card)
            score_c += rand_card
            if 11 in computer and score_c >= 21:
                player.remove(11)
                player.append(1)
                score_c -= 10

        while score_p <= 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                rand_card = random.choice(cards)
                player.append(rand_card)
                score_p += rand_card
                if 11 in player and score_p >= 21:
                    player.remove(11)
                    player.append(1)
                    score_p -= 10
                print(f"    Your cards: {player}, current score: {score_p}")
                print(f"    computer's first card: {computer[0]}")
            else:
                break
        
        print(f"    Your cards: {player}, final score: {score_p}")
        print(f"    Computer cards: {computer}, final score: {score_c}")
if score_p > 21:
    print("You went over. You lose ;o;")
elif score_c > 21:
    print("The computer went over, you win!")
elif score_p == score_c:
    print("Tied.")
elif score_c < score_p:
    print("YOU WIN!!")
elif score_c > score_p:
    print("You lost.")