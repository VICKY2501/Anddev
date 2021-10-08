import random
import time
option=["Snake","Water","Gun"]
r=0
def comapre(choice):
    
    r=random.choice(option)
    print("------------------------------------------\n")
    print("Computer Chooses------\n")
    time.sleep(2.5)
    print(r)
    print("------------------------------------------\n")
    if choice==1 and r=='Snake':
        print("You Won the game")
        print("--------------------------------")
        r=int(input("enter 1 to play again\n"))
        if r==1:
            print("-------LOCK YOUR CHOICES HERE---------")
            print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
            r=int(input("enter 1 to play again\n"))
            print("------------------------------------------\n")
            print("You choose------\n")
            print(choice)
            comapre(choice)
        else:
            print("again Entered a wrong input\n")    
        
        r=input("enter 1 to play again\n")
        if r==1:
            print("-------LOCK YOUR CHOICES HERE---------")
            print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
            r=int(input("enter 1 to play again\n"))
            print("------------------------------------------\n")
            print("You choose------\n")
            print(choice)
            comapre(choice)
        else:
            print("again Entered a wrong input\n")    

    elif choice==2 and r=='Water':
        print("You won the game")
        print("--------------------------------")
        r=input("enter 1 to play again\n")
        if r==1:
            print("-------LOCK YOUR CHOICES HERE---------")
            print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
            r=int(input("enter 1 to play again\n"))
            print("------------------------------------------\n")
            print("You choose------\n")
            print(choice)
            comapre(choice)
        else:
            print("again Entered a wrong input\n")    

    elif choice==3 and r=='Gun':
        print("You won the game")
        print("--------------------------------")
        r=input("enter 1 to play again\n")
        if r==1:
            print("-------LOCK YOUR CHOICES HERE---------")
            print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
            r=int(input("enter 1 to play again\n"))
            print("------------------------------------------\n")
            print("You choose------\n")
            print(choice)
            comapre(choice)
        else:
            print("again Entered a wrong input\n")


    else:
        print("Sorry You lost the Game")
        print("--------------------------------")
        r=int(input("enter 1 to play again\n"))
        if r==1:
            print("-------LOCK YOUR CHOICES HERE---------")
            print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
            r=int(input("enter 1 to play again\n"))
            print("------------------------------------------\n")
            print("You choose------\n")
            print(choice)
            comapre(choice)            
        else:
            print("again Entered a wrong input\n")

        
print("-------------------------Welcome-------------------")
print("-------LOCK YOUR CHOICES HERE---------")
print("(1) FOR SNAKE\n"+"(2) FOR WATER\n"+"(3) FOR GUN\n")
choice=int(input("Enter your choice No\n"))
print("------------------------------------------\n")
print("You choose------\n")
print(choice)

comapre(choice)
                





