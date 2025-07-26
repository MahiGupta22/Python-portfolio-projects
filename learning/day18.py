#keyword + module + keyowrd + things in module
from turtle import * #imports every class from the module
from random import choice , randint
#install new packages via terminal
#pip install heroes
#print(heroes.gen())
#keyword + module + keyword + alias name
#import turtle as t [module aliasing]
t = Turtle()

t.shape("turtle") #draw shape
t.color("red") #change color

def practise():
    for i in range(4): #make a square
        t.forward(100) #to move forward
        t.right(90) #to move right on an angle
        i+=1

def dashed_line():
    for i in range(5): #dashed line
        t.forward(10)
        t.penup() #to move untraceably
        t.forward(10)
        t.pendown() #to trace movement
        i+=1
        
colors=[
    "LightSeaGreen",
    "MediumTurquoise",
    "CadetBlue",
    "DarkTurquoise",
    "SteelBlue",
    "RoyalBlue",
    "MediumSlateBlue",
    "SlateBlue",
    "DarkSlateBlue",
    "DarkCyan",
    "SeaGreen",
    "DarkSeaGreen"
]
#t.width(15)
t.speed("fastest")
def draw_shape():
    for i in range(3,11):
        angle = 360 / i #make different shapes using angles
        t.color(choice(colors))
        #t.color(colors[i-3])
        for j in range(i):
            t.forward(100)
            t.left(angle)
def random_color():
    colormode(255)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color= (r,g,b)
    #t.color(r,g,b) to check
    return color

directions=[0,90,180,270]            
def walking():
    for i in range(300):
        #t.color(choice(colors))
        t.color(random_color())
        t.forward(30)
        t.setheading(choice(directions))

def spirograph(size):
    for i in range(360//size):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size)
draw_shape()

screen = Screen() #class asignment to a variable
screen.exitonclick()
