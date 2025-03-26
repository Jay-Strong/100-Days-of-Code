import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
temp_list = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for num in range(nr_letters):
    temp_list.append(random.choice(letters))
nr_symbols = int(input(f"How many symbols would you like?\n"))
for num in range(nr_symbols):
    temp_list.append(random.choice(symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for num in range(nr_numbers):
    temp_list.append(random.choice(numbers))

print(temp_list)
random.shuffle(temp_list)
print(temp_list)

password = ''.join(temp_list)
print(f"Your password is: {password}.")
print(len(password))
