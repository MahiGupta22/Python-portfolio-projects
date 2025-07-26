#hangman
import random
print("WELCOME TO THE HANGMAN GAME!")
while True:
    stages=['''
     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
    =======
    ''','''
     +---+
     |   |
     0   |
    /|\  |
    /    |
         |
    =======
    ''','''
     +---+
     |   |
     0   |
    /|\  |
         |
         |
    =======
    ''','''
     +---+
     |   |
     0   |
    /|   |
         |
         |
    =======
    ''','''
     +---+
     |   |
     0   |
     |   |
         |
         |
    =======
    ''','''
     +---+
     |   |
     0   |
         |
         |
         |
    =======
    ''','''
     +---+
     |   |
         |
         |
         |
         |
    =======
    ''','''
     +---+
         |
         |
         |
         |
         |
    =======
    ''']
    word_list=["apple","babycorn","cabbage","dimsum","fish","grape","hamburger","icecream"]
    chosen_word=random.choice(word_list)
    print(chosen_word)
    placeholder=""
    for position in range(0,len(chosen_word)):
        placeholder+="_ "
    print(placeholder)
    game_over=False
    correct_letters=[]
    n=-1
    while not game_over:
        guess=input("Guess the letter: ").lower()
        display=""
        for letter in chosen_word:
            if letter==guess:
                correct_letters.append(guess)
                display+=letter
            elif letter in correct_letters:
                display += letter
            else:
                display+="_ "
        if guess not in chosen_word:
            n-=1
            print(stages[n])
        print(display)

        if "_ " not in display:
            print("You WON")
            game_over=True
        if stages[n]==stages[0]:
            print("You LOST")
            game_over=True
    again=str(input("Do you want to play again?(y/n)"))
    if again.lower()=="y":
        continue
    elif again.lower()=="n":
        print("Exiting!!")
        break
    else:
        print("enter a valid input!")
        
