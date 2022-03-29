"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", [Kanye West", "Pete Davidson"])))
# Ddefine a function named contains 
# Two parameteers:
# 1. needle - the string we're searching for
# 2. haystacck - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:

    # Algorithm:
    # For each item in the haystack
    # Test if it is equal to the needle
    # if so, return True
    for item in haystack:
        if item == needle:
            return True 
# After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise 
    return False

    if __name__ == "__main__":
        main()