"""modules are just code files which defines variables and
function just like a class that defines attributes and methods"""

from turtle import *
timmy= Turtle()
print(timmy) #prints an object
timmy.shape("turtle")
timmy.color("burlywood4")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

"""PyPi.org is a online site on which we can search various modules
or packages used by developers all around to perform a particular
task or complete a project"""

from prettytable import PrettyTable
table = PrettyTable(["Name","Roll no."])
table.add_row(["foo", 12])
table.add_column("Class",["10B"])
print(table)

"""We can change attributes, add values using different functions that are
available on the website"""

