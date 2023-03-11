import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     plain_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         print(f"Old position: {position}, new position: {new_position}")
#         print(f"Old letter: {letter}, new letter: {alphabet[new_position]}")
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(text=text, shift=shift)
# elif direction == "decode":
#     decrypt(text=text, shift=shift)
# else:
#     print("Invalid direction")


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             print(f"{number} is divisible by {i}")
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)


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
