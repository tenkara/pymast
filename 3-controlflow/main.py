print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if (height >= 120):
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Path: 3-controlflow\main.py
print("Enter a number to check if it is odd or even.")
number = int(input("What is your number? "))
if (number % 2 == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")


print("Enter an year to check if it is a leap year.")
year = int(input("What is your year? "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if(height >= 120 and age >= 12):
    print("You can ride the rollercoaster!")
elif(height >= 120 and age < 12):
    print("You can ride the rollercoaster with a parent/guardian.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


