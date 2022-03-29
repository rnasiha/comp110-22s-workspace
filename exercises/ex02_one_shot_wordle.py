"""EX02 - One shot Wordle."""

__author__ = "730330522"

answer: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
correct_answer_msg: str = "Woo! You got it!"
wrong_answer_msg: str = "Not quite. Play again soon!"
length_error_msg: str = "That was not 6 letters! Try again."

input_word: str = input("What is your 6 letter guess?")
while len(input_word) != 6:
    print(f"{length_error_msg}")
    input_word = input("What is your 6 letter guess?")
if input_word == answer:
    print(f"{correct_answer_msg}")
else:
    print(f"{wrong_answer_msg}")
index_1: int = 0
result_emoji: str = "" 

while index_1 < len(input_word):
    if input_word[index_1] == answer[index_1]: 
        result_emoji = result_emoji + GREEN_BOX
    else:
        match: bool = False
        index_2: int = 0
        while index_2 < len(input_word):
            if input_word[index_1] == answer[index_2]:
                match = True
            index_2 = index_2 + 1
        if match:
            result_emoji = result_emoji + YELLOW_BOX
        else:
            result_emoji = result_emoji + WHITE_BOX
    index_1 = index_1 + 1 

print(f"{result_emoji}")