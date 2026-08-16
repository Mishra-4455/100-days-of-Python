import Ceasar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(Ceasar_art.logo)

def ceasar(initial_text, sh, option):
    final_text = ""
    for i in initial_text:
        if i not in alphabet:
            final_text += i
        else:
            pos = alphabet.index(i)
            if(option == 'encode'):
               final_text += alphabet[(pos+sh) % 26] 
            else:
               final_text += alphabet[(pos-sh) % 26]
    print(f"The {option}d text is {final_text}")
while 1<2:
    direction = input("Type 'encode' to encript, type 'decode' to decript:\n")
    text = input("Type your input:\n").lower()
    shift = int(input("Type your shift number:\n"))

    ceasar(initial_text=text, sh=shift, option=direction)
    way = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
    if way == "no":
        print("Goodbye!")
        break