fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
print(fruits)

students_height = input("Input a list of student heights ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

total_height = 0
for height in students_height:
    total_height += height
print(total_height)

number = int(input("How many students are there? "))
total_height = 0
for student in range(0, number):
    height = int(input("Enter student height: "))
    total_height += height 
print(f"Total height: {total_height}")
print(f"Average height: {round(total_height / number)}")

# max_number
# Write your code below this row 👇
scores = [78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
avg_score = 0
number_of_scores = 0
for score in scores:
        if score > max_score:
            max_score = score
print(max_score)

# add numbers from 1 to 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(0, nr_letters):
    password += random.choice(letters) 
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
for number in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
for char in range(0, nr_letters + nr_symbols + nr_numbers):
    password += random.choice(letters + symbols + numbers)
print(password)

