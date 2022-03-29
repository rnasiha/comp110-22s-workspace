"""EX06- Dictionary skeleton functions."""

__author__ = "730330522"


def invert(dict_in: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    my_dict = {}
    for x in dict_in:
        val = dict_in[x]   
        if val in my_dict:
            raise KeyError("Duplicate Key!")
        my_dict[val] = x 
    return (my_dict)


def favorite_color(dict_in: dict[str, str]) -> str:
    """Favorite colors function."""
    my_dict = {}
    for x in dict_in:
        colr = dict_in[x]
        if colr not in my_dict:
            my_dict[colr] = 1 
        else:
            my_dict[colr] = my_dict[colr] + 1 
    max_key = max(my_dict, key=my_dict.get)
    return(max_key)


def count(my_list: list[str]) -> dict[str, int]:
    """Count function."""
    my_dict = {}
    for x in my_list:
        if x not in my_dict:
            my_dict[x] = 1 
        else: 
            my_dict[x] = my_dict[x] + 1
    return (my_dict)
