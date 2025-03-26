print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
breadsticks = input("Do you want breadsticks? Y or N: ").upper()

bill = 0
invalid = False
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    invalid = True

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

if breadsticks == "Y":
    bill += 4.99

tax = (.06 * bill)
bill += tax

if invalid:
    print("You've entered an invalid size.")
else:
    print(f"Your final bill is: ${bill:.2f}.")