#!/usr/bin/python3
""" This module contains a function (pascal_triangle(n)) that
Generate Pascal's triangle up to the n-th row."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n-th row.

    Parameters:
    n (int): The number of rows of Pascal's triangle to generate.

    Returns:
    list: A list of lists containing the values of Pascal's triangle.
           Each inner list represents a row of the triangle.
    """
    # Return an empty list if n is less than or equal to 0.
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row.

    # Handle the case where only one row is needed.
    if n == 1:
        return triangle

    triangle.append([1, 1])
    row = 2

    # Construct each subsequent row until reaching n rows.
    while row < n:
        # Initialize a new row with 1's.
        new_row = populate_list(row + 1)
        # Populate the new row using the values from the previous row.
        for idx in range(1, len(new_row) - 1):
            # Skip the first and last element.
            new_row[idx] = triangle[row - 1][idx - 1] + triangle[row - 1][idx]

        triangle.append(new_row)
        row += 1

    return triangle


def populate_list(n):
    """
    Create a list of length n initialized with 1's.

    Parameters:
    n (int): The length of the list to create.

    Returns:
    list: A list of length n filled with the integer 1.
    """
    return [1] * n
