# TODO
from cs50 import get_string

# Initialize necessary variables
text = get_string("Text: ")
letters = 0
words = 1
sentences = 0

# Count quantity of letters, words, sentences
for i in text:
    if i.isalpha():
        letters += 1
    if i == ' ':
        words += 1
    if i == '.' or i == '?' or i == '!':
        sentences += 1

# Calculate Coleman-Liau Index
CLI = 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8

# Define Grade
if CLI < 1:
    print("Before Grade 1")
elif int(CLI) >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(CLI)}")
