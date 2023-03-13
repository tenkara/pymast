numbers = range(1, 10)
squares = [n**2 for n in numbers]
print(squares)
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

names = ['Alice', 'Bob', 'Charlie', 'Debbie']
cap_names = [name.upper() for name in names if len(name) > 4]
print(cap_names)

with open('file1.txt') as file1:
    file1_nums = file1.readlines()
with open('file2.txt') as file2:
    file2_nums = file2.readlines()


result = [int(num) for num in file1_nums if num in file2_nums]
print(result)
