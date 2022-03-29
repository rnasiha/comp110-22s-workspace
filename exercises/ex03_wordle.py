"""EX03 - Six guess Wordle."""

__author__ = "730330522"


def contains_char(word: str, char: str) -> bool:
    """Returns true if character is found in word, false if not."""
    assert len(char) == 1
    index = 0
    while (index < len(word)):
        if word[index] == char:
            return True
        index += 1
    return False 


def emojified(guess: str, answer: str) -> str:
    """Inputs a guess word and the correct word, returns the "emojified" version of the guess."""
    assert len(guess) == len(answer)
    ans = ""
    index = 0
    while index < len(guess):
        if guess[index] == answer[index]:
            ans = ans + "\U0001F7E9"
        if not guess[index] == answer[index] and contains_char(answer, guess[index]):
            ans = ans + "\U0001F7E8"
        if not guess[index] == answer[index] and not contains_char(answer, guess[index]):
            ans = ans + "\U00002B1C"
        index = index + 1
    return ans


def input_guess(length: int) -> str:
    """Prompts the user to type in a guess with n letters. Returns the word if it is the right length."""
    input_word: str = input("Enter a " + str(length) + " character word: ")
    while len(input_word) != length:
        input_word = input("That wasn't " + str(length) + " chars! Try again:")
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    word = "codes"
    won = False

    while (turns <= 6 and not won):
        print("=== Turn " + str(turns) + "/6 ===")
        guess = input_guess(5)
        print(emojified(guess, word))
        if guess == word:
            print("You won in " + str(turns) + "/6 turns!")
            won = True
            return
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()