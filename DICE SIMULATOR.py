import random as r

print("Dice Rolling Game \n Press enter to start the game")
s=input()

flag = True

if s == "":
    while flag == True:
        a=r.randint(1,6)
        print ("BOT: ",a)
    
        print("Your turn! Press enter")
        i=input()
        if i == "":
            b=r.randint(1,6)
            print("YOU: ",b)
            
        if a<b:
            print("YOU WON :)")
        elif a==b:
            print ("IT'S A DRAW!!!!")
        else:
            print("YOU LOSE :(")

        choice=input("Do you want to play again?(Y/N)")
    
        if choice == "Y" or choice == "y":
            flag = True
        else:
            flag = False
            
            print("Thanks for playing!")