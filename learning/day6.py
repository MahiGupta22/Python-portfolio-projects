#ESCAPE THE MAZE
def turn_right():
    for _ in range(3):
        turn_left()

def front_isclear():
    move()
turn_left()

while not at_goal():
    if right_is_clear() and front_is_clear():
        turn_right()
        if is_facing_north():
            move()
        else:
            for _ in range(3):
                turn_right()
            move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
