print("Welcome to Rock, paper and Scissors, Ready to beat the unbeatable odds?\nThere are 1M players playing rn and you are fighting for the top")
player = input("I am totally going Rock...or am I? :)\nRock, paper, Scissorsss...... shoot! R,P,S?")
print("ROCK!")
if player == "P":
    print("Congratulations on passing the first round!\nYou surpassed 667,000 of the People who started the Game with you")
    print("Ready for the next round?\n I am definetly going rock again :)")
    player = input("Readyyyy Rock, paper, scissorssss......... shoot! R,P,S?\n")
    if player == "P":
        print("Paper Beats Rock AGAIN!\nYou've now survived the second great cull and now are 1 in 111,111 players!")
        print("Lets begin with the third round. I am gonna go rock again, Tripple bluff? maybe")
        print("Readyyyy... Rock, paper, scissor andddd... shoot! R,S,P?\n")
        if player == "P":
            print("Congratulations you didn't fall for the tripple bluff!\nYou are now in the top 40k people club :D")
            print('Now onto this round, I will give you a hint.. i will go rock again :)\n"NO HE COULD,NT QUADRUPLE BLUFF" i hear you say.')
            print("Maybe, maybe not, lets go then Rock, paper, scissor anddddd shoot! R,P,S?\n")
            if player == "P":
                print("HAHHAHAHAHAAHAAH, I DID GO ROCK AGAIN, and seems like you beat it as well.\nNow you are in the top 12k people.")
                print("Now might as well consider youself a winner. Congratulations you beat me!")
            else:
                print("SHIIIIIIIII YOU FELL FOR THE QUADRUPLE BLUFF, I was about to give up there.\nWelp so close yet so far.")
                print("Better luck next time dude :)")
        else:
            print("AWE MAN YOU FELL FOR THE TRIPPLE BLUFF HECKKKK, welp better luck next time :)")
    else:
        print("AWE MAN YOU FELL FOR THE DOUBLE BLUFF HECKKKK, welp better luck next time :)")
else:
    print("Awwwww you lost on the first round. Don't worry Better luck next time :)")