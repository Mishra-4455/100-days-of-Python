import tkinter


window = tkinter.Tk()
# On how to create a window(GUI) with a texton title
window.title("My first GUI")
window.minsize(width= 800, height=500)


# On how to write in the GUI
my_lable = tkinter.Label(text= "I am a Lable", font=("Arial", 24, "bold"))
my_lable.grid(row= 0, column=0)


# After the info from the "sandbox" we now know that we can just treat these as a dictionary keywords
# so now we can do this
my_lable["text"] = "New_Text"
# OR
# my_lable.config(text= "Now_this_is_some_new_Text")


# On how to create a button
button = tkinter.Button(text= "click me")
button2 = tkinter.Button(text = "click me2")
button.grid(row=1, column=1)
button2.grid(row=0, column=2)


# On how to add function to a button
def click():
    print("I got clicked")
button.config(command= click)


# On how to create a input box to input anything
input_user = tkinter.Entry()
input_user.grid(row=2, column=3)
def user_inp():
    s = input_user.get() # Returns input from the user in form of a string
    my_lable.config(text= s)
button.config(command= user_inp)

'''The taking input and then updating the text on the screen has to be done
   incorporating both the button and input_box together cause it cant detect
   a enter click yet.'''

'''About positioning stuff in the window, there are three standard systems that are used to position stuff in the window i.e., manage where goes what
   These are: pack, place and grid
   pack: It just has 4 configurations to place stuff top, bottom, left, right and if you place 2 on the top for example they will be placed
   one below the first one
   place: It requres you to enter the exact x and y coordinate to position the text, button, etc. and the top left acts as (0,0)
   grid: It splits the window into a grid with rows and cloumns to manage the placement of the text, buttons, etc'''

# On how to keep a GUI open unless clicked the cross button to close
window.mainloop()   