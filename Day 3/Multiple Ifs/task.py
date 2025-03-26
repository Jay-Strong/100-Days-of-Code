print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))

if height >= 120:
    total = 0
    print("You can ride the rollercoaster!\n")
    age = int(input("What is your age? "))
    if age <= 12:
        total = 5
    elif age <= 18:
        total = 7
    else:
        total = 12
    photo = input("Purchase a photo for $3 (y or n)? ")
    if photo == "y":
        total += 3
    print(f"Your total is ${total} ")
else:
    print("Sorry you have to grow taller before you can ride.")


