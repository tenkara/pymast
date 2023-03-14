input = input(f"enter a sentence to count the words: ")
words = input.split()
word_count = {word: words.count(word) for word in words}
letter_count = {word: len(word) for word in words}
print(word_count)
print(letter_count)