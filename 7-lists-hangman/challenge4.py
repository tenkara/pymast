import random
lives = 6
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")
print(display)
while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            break
        print(f"You have {lives} lives left")