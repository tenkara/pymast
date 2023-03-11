import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1 - create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")
print(display)

# guess = input("Guess a letter: ").lower()    

# TODO-2 - Loop through each position in the chosen_word;
# if the letter is that position matches the guess then reveal that letter in the display at that position
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         display[i] = guess
# print(display)

# TODO-3 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)