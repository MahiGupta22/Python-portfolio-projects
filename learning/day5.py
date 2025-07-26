#highest score of teams
teams=int(input("enter the number of teams:"))
arr=[]
for i in range(0,teams):
    x=int(input("enter the points scored by the team :"))
    arr.append(x)
maxm=0
for score in arr:
    if score>maxm:
        maxm=score

print(maxm)
    
#FizzBuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#Password Generator
import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=['!',"@","#","$","%","&","(",")","*","?","+"]
print("Welcome to the pyPassword Generator")
num_letters=int(input("how many letters would you like in your password?\n"))
num_symbols=int(input("how many symbols would you like in your password?\n"))
num_numbers=int(input("how many numbers would you like in your password?\n"))
password=[]
for char in range(0,num_letters):
    password.append(random.choice(letters))
for char in range(0,num_symbols):
    password.append(random.choice(symbols))
for char in range(0,num_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
passwords=""
for pw in password:
    passwords+=pw
print(passwords)
