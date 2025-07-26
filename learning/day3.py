#bmi calculator
weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<25:
    print("normal weight")
else:
    print("overweight")

#rollercoaster
print("welcome to the rollercoaster!")
height=int(input("What is your height in cms? "))
if height >= 120:
    print("you can ride the rollercoaster")
    age= int(input("what is your age? "))
    if age<=12:
        print("please pay $5 for child ticket")
    elif age<=18:
        print("please pay $7 for youth ticket")
    else:
        print("please pay $12 for adult ticket")
else:
    print("Sorry you'll have to grow taller before you can ride")

#pizza order
print("Welcome to Python Pizza Deliveries!")
size=input("what size pizza do you want? S,M or L:")
pepperoni=input("do you want pepperoni on your pizza? Y or N:")
extra_cheese=input("do you want extra cheese? Y or N:")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("make an appropriate selection")
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print("your final bill is: ",bill)






