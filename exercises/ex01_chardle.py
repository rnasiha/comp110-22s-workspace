"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730330522"

input_word: str = input("Enter a 5-character word:")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters") 
    exit() 
input_character: str = input("Enter a single character:")
if len(input_character) != 1:
    print("Error: Character must be a single character.") 
    exit() 
print("Searching for", input_character, "in", input_word)
n = 0
if input_word[0] == input_character:
    print(input_character, "found at", "index 0")
    n = n + 1
if input_word[1] == input_character:
    print(input_character, "found at", "index 1")
    n = n + 1
if input_word[2] == input_character:
    print(input_character, "found at", "index 2")
    n = n + 1
if input_word[3] == input_character:
    print(input_character, "found at", "index 3")
    n = n + 1
if input_word[4] == input_character:
    print(input_character, "found at", "index 4")
    n = n + 1
if n == 0:
    print("No instances of", input_character, "found in", input_word)
else:
    if n == 1:
        print(n, "instance of", input_character, "found in", input_word)
    else:
        print(n, "instances of", input_character, "found in", input_word)
