MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resourceManage(coffee):
    for ingred in MENU[coffee]["ingredients"]:
        resources[ingred] -= MENU[coffee]["ingredients"][ingred]

def resourceCheck(coffee):
    for ingred in MENU[coffee]["ingredients"]:
        if not resources[ingred] >= MENU[coffee]["ingredients"][ingred]:
            print(f"Sorry there is not enough {ingred}.")
            return -1
    return 0
            

def calcMoney(cost):
    global profit
    pennies = int(input("Enter the number of pennies:"))
    nickel = int(input("Enter the number of nickel:"))
    dimes = int(input("Enter the number of dimes:"))
    quarter = int(input("Enter the number of quarter:"))
    total = (0.25*quarter + 0.1*dimes + 0.05*nickel + 0.01*pennies)

    if cost>total:
        return -1
    else:
        profit += cost
        return round(total-cost, 2)

while True:
    option = input("What would you like? (espresso/latte/cappuccino):")
    if option == "espresso" or option == "latte" or option == "cappuccino":
        x = resourceCheck(option)
        if x != -1:
            print("Please insert coins.")
            money = calcMoney(MENU[option]["cost"])
            if money == -1:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is {money} in change.")
                resourceManage(option)
                print(f"Here is your {option}, Enjoy")
            
    elif option == "report":
        for ingred in resources:
            print(f"{ingred}: {resources[ingred]}")
        print(f"Money: ${profit}")

    elif option == "off":
        break

    else:
        print("Enter a valid input.")