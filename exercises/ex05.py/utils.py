"""EX05 - Skeleton Code."""

__author__ = "730330522"


def only_evens(integers: list[int]) -> list:
    """ Returns only even numbers in the list."""
    result = []
    if len(integers) == 0:
        return result   
    for number in integers:
        if number % 2 == 0:
            result.append(number)
    return result


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(only_evens(numbers)) 


def sub(x: list, start: int, end: int) -> list:
    """Generates a List which is a subset of the given list, between the specified start index and the end index - 1.""" 
    result = []
    if start < 0: 
        start = 0
    if end > len(x):
        end = len(x)
    i = start 
    while i < end:
        result.append(x[i])
        i += 1 
    return result 


print(sub(numbers, 2, 8))


def concat(list_1: list[int], list_2: list[int]) -> list:
    """Generates a new List which contains all of the elements of the first list followed by all of the elements of the second list. """
    result = []
    for i in list_1:
        result.append(i)
    for i in list_2:
        result.append(i)
    return result


single_item: list[int] = [1]

print(concat(numbers, numbers))