"""Dictionary related utility functions."""

__author__ = "730330522"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
 
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]  #
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based able with only the first `N` (a parameter) rows of data for each column."""
    dict_empty: dict[str, list[str]] = {}

    for column in table:
        n_values: list[str] = []
        for item in range(rows):
            if item < len(table[column]):
                n_values.append(table[column][item])
        dict_empty[column] = n_values

    return dict_empty


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    dict_empty: dict[str, list[str]] = {}

    for column in col_names:
        dict_empty[column] = table[column]
    return dict_empty


def concat(table: dict[str, list[str]], two_col: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    dict_empty = dict[str, list[str]] = {}
    for column, val in table.items():
        dict_empty[column] = val
    for column, val in two_col.items():
        for col in table:
            bool = False
            if column == col:
                bool = True
            if bool: 
                dict_empty[column] = table[column] + two_col[column]
            else:
                dict_empty[column] = two_col[column]
    return dict_empty


def count(values: list[str]) -> dict[str, int]:
    """Produce a dict[str, int] where each key is a unique value in the given list.""" 
    dict_empty: dict[str, int] = {}

    for value in values:
        if value in dict_empty:
            dict_empty[value] += 1
        else:
            dict_empty[value] = 1
            
    return dict_empty