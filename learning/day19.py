#event listeners
from turtle import Turtle, Screen
screen= Screen()
'''
t= Turtle()
def move_forwards():
    t.forward(10)
screen.listen()
screen.onkey(key="space", fun=move_forwards) #functions as inputs with () {higher order functions}
#moves when press space bar
#higher order functions use other functions
#there are two types of arguments: positional and argument
'''
#turtle coordinate system
'''
screen.setup(width=500,height=400)
user_bet= screen.textinput(title="Gamble",prompt="Which turtle will win the race? enter the color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-238,y=y_positions[turtle_index])
'''
screen.exitonclick()
