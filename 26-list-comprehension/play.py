numbers = range(1, 10)
squares = [n**2 for n in numbers]
print(squares)

names = ['Alice', 'Bob', 'Charlie', 'Debbie']
cap_names = [name.upper() for name in names if len(name) > 4]
print(cap_names)