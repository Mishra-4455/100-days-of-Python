Std_scores = input("Input a list of student scores: ").split( )
for n in range(0, len(Std_scores)):
    Std_scores[n] = int(Std_scores[n])

max = Std_scores[0]
for score in Std_scores:
    if max < score:
        max = score

print(f"The Highest score in the class is: {max}")