def format_name():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    return f"{first_name.title()} {last_name.title()}"

print(format_name())

