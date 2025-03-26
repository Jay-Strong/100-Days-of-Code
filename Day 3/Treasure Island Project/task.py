print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You are at a crossroad. Which direction would you like to go? "
                'Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You have arrived at a lake. '
                    'There is an island on the lake. '
                    'Do you wait for a boat or swim across? '
                    'Type "wait" or "swim"\n').lower()
    if choice2 == "wait":
        choice3 = input('A boat arrives to take you to the island. '
                        'Once you arrive there is a house with three doors. '
                        'One red, one yellow, and one blue. '
                        'Which door do you choose? '
                        'Type "red", "yellow", or "blue"\n').lower()
        if choice3 == "red":
            print("You are burned by fire. Game over.")
        elif choice3 == "blue":
            print("You are eaten by wolves. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        else:
            print("You have chosen a door that doesn't exist. Game over.")
    else:
        print("You realize it's too far and you drown. Game over.")
else:
    print("You fall into a hole. Game over.")
