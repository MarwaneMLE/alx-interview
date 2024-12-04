#!/usr/bin/python3
# Tasks: 0. Island Perimeter


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    Args:
        grid(list): list of integrs
    """

    perimeter = 0
    for row_index in range(len(grid)):
        for cell_index in range(len(grid[0])):
            current_cell = grid[row_index][cell_index]
            if not current_cell:
                continue

            if not row_index:
                upper_cell = None
            else:
                upper_cell = grid[row_index - 1][cell_index]
            if not cell_index:
                left_cell = None
            else:
                left_cell = grid[row_index][cell_index - 1]
            cell_perimeter = 4
            if upper_cell:
                cell_perimeter = cell_perimeter - 2
            if left_cell:
                cell_perimeter = cell_perimeter - 2
            perimeter = perimeter + cell_perimeter
    return perimeter
