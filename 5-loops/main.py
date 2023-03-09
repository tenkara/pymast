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
