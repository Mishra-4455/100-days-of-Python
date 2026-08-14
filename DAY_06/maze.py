def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not wall_on_right():
    if front_is_clear():
        turn_left()
    move()

while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    if not at_goal():
        turn_right()
        move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
