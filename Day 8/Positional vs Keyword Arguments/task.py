# Functions with input

# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")

user_name = input("Enter your name: ")
user_location = input("Enter your location: ")


# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}?")


# greet_with(name, location)


def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with(location=user_location, name=user_name)
