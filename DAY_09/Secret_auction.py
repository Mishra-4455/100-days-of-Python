auction = {}
print("Welcome to the auction program.")

def users():
    name = input("What's your name? ")
    bid = int(input("What's your Bid? $"))
    auction[name] = bid

users()
while 1<2:
    option = input("Are there any other biddrs? Type 'yes' or 'no'.\n")
    if option == "yes":
        print("\n" * 10)
        users()
    else:
        break

cbidder = ""
cbid = 0
max = 0
for biddrs in auction:
    cbid = auction[biddrs]
    if max < cbid:
        max = cbid
        cbidder = biddrs

print(f"\nThe winner is {cbidder} with a bid of ${max}")