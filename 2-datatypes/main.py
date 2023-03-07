#String

print("Hello"[4])

#Integer

print(123 + 345)


#Float

3.14159

#Boolean


True
False

#Type Error
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

#Type Error
a = float(123)
print(type(a))

#Type Error
print(70 + float("100.5"))

#Type Error
print(str(70) + str(100))

#Type Error
print(int("100") + int("100"))

#Type Error
print(123 + float("456.789"))

#Type Error
print(str(123) + str(456.789))

#Type Error
print(123 + int("456"))

#Type Error
print(str(123) + str(456))

num = input("Enter a two digit number: ")
print(f"Your number is {num}")
print(f"Your number is {int(num[0]) + int(num[1])}")







