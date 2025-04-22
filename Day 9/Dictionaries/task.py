programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print("")
for item in programming_dictionary:
    print(f"{item}: {programming_dictionary[item]}")

programming_dictionary["Loop"] = "Repeating the same instructions until an ending condition is met."
print("")
for item in programming_dictionary:
    print(f"{item}: {programming_dictionary[item]}")
