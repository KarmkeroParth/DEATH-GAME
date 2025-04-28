print(r'''
*******************************************************************************
 ______________
|\ ___________ /|                                          
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   |   | |
| | |/    |   | |
| |    /] |   | |
| |   [/ ()\  | |
| |       | \,^%---
| |       | <\/ \ Hello!
| |       |<  | |
| |      ,'<  | |
| |   ,' ^^|\ | |
|_|,'_____/__\|_| 
*******************************************************************************
''')
print("Welcome to death game.")
print("Your mission is to find the right door or you will die. :) ")
print("You have to choose either left or right or you will die :) ")
first = input("left or right? \n")
if first.casefold() == "right":
    print("You have chosen the right door. :)")
    second = input("left or right? \n")
    if second.casefold() == "left":
        print("You have chosen the right door. :)")
        print("Welcome to the last door. ")
        Third = input("left or right? \n")
        if Third.casefold() == "left":
            print("You have chosen the right door. :)")
        else:
            print("You have been fallen into a hole. :)")
        print("Oh wow you have survived this game. Here is your gift. LIFE  :)")
        print('see you again. :)')
    else:
        print("You have been eaten by a hungry lion. :)")
else:
    print("You have been burned into ashes. :)")