#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def can_place_queen(positions, current_row, current_col):
    for row in range(current_row):
        col = positions[row]
        if col == current_col or \
           col - row == current_col - current_row or \
           col + row == current_col + current_row:
            return False
    return True


def solve_nqueens(N):
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
