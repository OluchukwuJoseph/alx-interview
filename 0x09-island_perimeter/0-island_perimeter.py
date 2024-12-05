#!/usr/bin/python3
""" This module contains the `island_perimeter` function. """
from typing import List


def check_top(grid: List[List[int]], row_idx: int, idx: int) -> bool:
    """
    Checks if the cell directly above the current cell is land (1).

    Args:
        grid: The 2D list representing the grid (island map).
        row_idx: The row index of the current cell.
        idx: The column index of the current cell.

    Returns:
        bool: True if the cell above the current cell is land (1),
            otherwise False.
    """
    # Check if the current row is the first row (no cell above it)
    if (row_idx - 1 < 0):
        return False
    # Return True if the cell above is land (1), else return False
    return True if grid[row_idx - 1][idx] == 1 else False


def check_left(grid: List[List[int]], row_idx: int, idx: int) -> bool:
    """
    Checks if the cell directly to the left of the current cell is land (1).

    Args:
        grid: The 2D list representing the grid (island map).
        row_idx: The row index of the current cell.
        idx: The column index of the current cell.

    Returns:
        bool: True if the cell to the left is land (1), otherwise False.
    """
    # Check if the current column is the first column
    if (idx - 1 < 0):
        return False
    # Return True if the cell to the left is land (1), else return False
    return True if grid[row_idx][idx - 1] == 1 else False


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculates the perimeter of an island on a 2D grid.

    Args:
        grid: The 2D list representing the grid (island map).

    Returns:
        int: The perimeter of the island formed by 1's.

    This function works by counting the number of edges of each land cell (1)
    that are not adjacent to other land cells.
    Each land cell starts with 4 potential sides contributing to the perimeter,
    and if there is a neighboring land cell (to the top or left),
    it subtracts 2 from the perimeter for each shared edge.
    """
    if (grid is None):
        return 0

    perimeter = 0

    for row_idx, row in enumerate(grid):
        for idx, cell in enumerate(row):
            if cell == 1:  # If the current cell is land
                perimeter += 4  # Add 4 to the perimeter for each land cell

                # Check if there is land above the current cell
                if check_top(grid, row_idx, idx):
                    perimeter -= 2  # Subtract 2 for the shared top edge

                # Check if there is land to the left of the current cell
                if check_left(grid, row_idx, idx):
                    perimeter -= 2  # Subtract 2 for the shared left edge

    return perimeter
