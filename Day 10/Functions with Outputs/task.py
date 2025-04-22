def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


first = input("Enter first name: \n")
last = input("Enter last name: \n")

formatted_name = format_name(first, last)

print(formatted_name)
