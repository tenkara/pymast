def add(**args):
    sum = 0
    for key, value in args.items():
        print(key, value)
        sum = sum + value
    print(sum)
    print(args)
    print(type(args))

# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
add(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)

def add(*numbers):
    sum = 0
    for value in numbers:
        print(value)
        sum = sum + value
    print(sum)
    print(numbers)
    print(type(numbers))

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
