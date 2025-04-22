def my_function():
    for i in range(1, 20 + 1):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop is iterating through number range 1-19

# 2. When is the function meant to print "You got it"?
# When the iteration variable 'i' is equal to a value of 20

# 3. What are your assumptions about the value of i?
# That it is initialized with a value of 1 in the for loop header
# That it is assigned to the next number in the sequence upon each iteration
# That the print statement will never be executed because 'i' will only ever reach
# a value of 19 and the loop will terminate before 'i' == 20.
