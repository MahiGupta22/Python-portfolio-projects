#bmi calculator
height = 1.65 
weight = 84
bmi = weight/ (height**2)
print(bmi)

#tip calculator
print("welcome to the tip calculator")
bill=float(input("what was the total bill?"))
tip=int(input("what percentage tip would you like to give? 10 12 15 "))
people=int(input("how many people to split the bill?"))
bill_with_tip=(tip/100) * bill + bill
per_person= bill_with_tip/people
final=round(per_person,2)
print("each person should pay:",final)


