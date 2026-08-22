import random
import art
import game_data

#function ot get a random entry from game data
#to diaplay the full data of each of the competitors
#to compare two entries side by side and compare their followers
#get user input and check if it alligns with the actual comparisn
#if yes then put score +1 else game ends
#The game data is a list of dictionaries

print(art.logo)

score = 0
def getcontender ():
    '''Gets a contender form the game_data file to compare to another'''
    p = random.choice(game_data.data)
    c = []
    for key in p:
        c.append(p[key])
    return c

def getmax(a, b):
    '''Gets maximum number of followers from the two contenders'''
    if a>b:
        return a
    else:
        return b

def compare ():
    global score
    c1 = getcontender()
    c2 = getcontender()

    print(f"Compare A: {c1[0]}, a {c1[2]}, from {c1[3]}")
    print(art.vs)
    print(f"Compare B: {c2[0]}, a {c2[2]}, from {c2[3]}")
    choice = input("Who has more followers?Type 'A' or 'B': ")
    max  = getmax(c1[1], c2[1])
    if choice == 'A':
        if max == c1[1]:
            score += 1
            print("\n"*20)
            print(art.logo)
            print(f"You are right! Current score: {score}")
            compare()
        else:
            print("\n"*30)
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        if max == c2[1]:
            score += 1
            print("\n"*20)
            print(art.logo)
            print(f"You are right! Current score: {score}")
            compare()
        else:
            print("\n"*30)
            print(f"Sorry, that's wrong. Final score: {score}")

compare()