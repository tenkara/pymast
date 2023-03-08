import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

random_integer = random.randint(1, 100)
print(random_integer)

# Heads or Tails
random_integer = random.randint(0, 1)
if random_integer == 1:
    print("Heads")
else:
    print("Tails")

# Rock, Paper, Scissors
# 0 = Rock
# 1 = Paper
# 2 = Scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")

        


