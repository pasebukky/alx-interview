#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """
    Prints the usage message and exits the program with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_number(n):
    """
    Checks if the given input is a valid integer.
    Args:
    n (str): The input to check.

    Returns:
    bool: True if n is a valid integer, False otherwise.
    """
    try:
        int(n)
        return True
    except ValueError:
        return False


def can_place_queen(positions, current_row, current_col):
    """
    Checks if a queen can be placed at the given row and column
    without being attacked.
    Args:
    positions (list): Current positions of the queens.
    current_row (int): The row to place the queen.
    current_col (int): The column to place the queen.

    Returns:
    bool: True if the queen can be placed, False otherwise.
    """
    for row in range(current_row):
        col = positions[row]
        if col == current_col or \
           col - row == current_col - current_row or \
           col + row == current_col + current_row:
            return False
    return True


def solve_nqueens(N):
    """
    Solves the N queens problem using backtracking.
    Args:
    N (int): The size of the chessboard (NxN).

    Returns:
    list: A list of all possible solutions, each solution is a
    list of column positions for each row.
    """
    def place_queens(row):
        if row == N:
            results.append(positions[:])
            return
        for col in range(N):
            if can_place_queen(positions, row, col):
                positions[row] = col
                place_queens(row + 1)

    results = []
    positions = [-1] * N
    place_queens(0)
    return results


def format_results(results):
    """
    Formats the results into the required output format.
    Args:
    results (list): A list of all possible solutions.
    Returns:
    list: A list of formatted solutions, each solution
    is a list of [row, col] pairs.
    """
    formatted_results = []
    for solution in results:
        formatted_solution = []
        for row, col in enumerate(solution):
            formatted_solution.append([row, col])
        formatted_results.append(formatted_solution)
    return formatted_results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    N = sys.argv[1]
    if not is_valid_number(N):
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    formatted_solutions = format_results(solutions)
    for solution in formatted_solutions:
        print(solution)
