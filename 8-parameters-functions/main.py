import math

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print(f"{number} is divisible by {i}")
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


# def greet():
#     print("Hello")
#     print("Good Morning")
#     print("How are you?")

# # Call the function
# greet()

# # Compare this function from 6-functions\challenge1.py:

# def greet_with_name(name = "Guest"):
#     print(f"Hello {name}")
#     print("Good Morning")
#     print("How are you?")

# # Call the function
# greet_with_name("Raj")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# # Call the function
# greet_with("Raj", "India")
# greet_with(location = "India", name = "Raj")

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")

# # Call the function
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)
