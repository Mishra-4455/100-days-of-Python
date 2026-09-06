import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {rows.letter : rows.code for (index, rows) in alphabets.iterrows()}
# print (alpha_dict)
string = input("Enter the word to be converted:").upper()
soln  = [alpha_dict[s] for s in string]
print(soln)