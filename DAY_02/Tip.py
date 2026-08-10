print("Welcome to the tip calculator.")
bill = float(input("What was the total Bill? $"))
percent = int(input("What persantage tip would you like to give? 10, 12 or 15? "))
peeps = int(input("How many people split the bill? "))

tip =  round((bill / peeps) * (1 + (percent/100)), 2)
print(f"Each person should pay :${tip}")