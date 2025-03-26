import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selections = [rock, paper, scissors]
rand_index = random.randint(0, 2)
user_selection = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))

if 0 <= user_selection <= 2:
    print(selections[user_selection])


comp_selection = rand_index
print("\n Computer chose:")
print(selections[rand_index])

if user_selection < 0 or user_selection >= 3:
    print("You chose an invalid number.")
elif comp_selection == 0 and user_selection == 2:
    print("You lose.")
elif user_selection == 0 and comp_selection == 2:
    print("You win.")
elif comp_selection < user_selection:
    print("You win.")
elif comp_selection > user_selection:
    print("You lose.")
elif comp_selection == user_selection:
    print("It's a draw.")
