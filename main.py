import re

# Read the text from the book
with open('book.txt', 'r') as f:
    text = f.read()

# Split the text into a list of words
words = [word for word in re.split(r'[^a-zA-Z]', text) if word]

# Create a new list that only contains words that are longer than 10 characters in length and are capitalized (first letter)
long_capitalized_words = [word for word in words if len(word) > 10 and word[0].isupper()]

print(long_capitalized_words)