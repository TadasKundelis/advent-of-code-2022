import heapq
from copy import deepcopy
from typing import List, Tuple, Set
from collections import namedtuple

with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

Square = namedtuple('State', ['row', 'col', 'height'])
Matrix = List[List[str]]


def solve(matrix: Matrix, *starting_squares: Square) -> int:
    end_row, end_col = find_square_positions(matrix, 'E')[0]
    matrix[end_row][end_col] = 'z'
    heap = []
    visited = set()

    for square in starting_squares:
        heapq.heappush(heap, (0, square))
        visited.add((square.row, square.col))

    while len(heap) > 0:
        current_cost, current_state = heapq.heappop(heap)
        next_squares = find_next_squares(current_state, matrix, visited)

        for next_square in next_squares:
            if next_square.row == end_row and next_square.col == end_col:
                return current_cost + 1
            visited.add((next_square.row, next_square.col))
            heapq.heappush(heap, (current_cost + 1, next_square))


def solve_part1(matrix: Matrix) -> int:
    start_row, start_col = find_square_positions(matrix, 'S')[0]
    start_square = Square(start_row, start_col, height=ord('a'))
    return solve(matrix, start_square)


def solve_part2(matrix: Matrix) -> int:
    starting_squares = []

    for start_row, start_col in find_square_positions(matrix, 'S', 'a'):
        starting_squares.append(Square(start_row, start_col, height=ord('a')))

    return solve(matrix, *starting_squares)


def find_square_positions(matrix: Matrix, *square_names: str) -> List[Tuple[int, int]]:
    positions = []
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] in square_names:
                positions.append((row, col))

    return positions


def find_next_squares(current_square: Square, matrix: Matrix, visited: Set[Tuple[int, int]]) -> List[Square]:
    row_modifier = [-1, 0, 1, 0]
    col_modifier = [0, 1, 0, -1]

    next_squares = []

    for i in range(4):
        new_row = current_square.row + row_modifier[i]
        new_col = current_square.col + col_modifier[i]

        if out_of_bounds(new_row, new_col, matrix):
            continue

        next_square = Square(new_row, new_col, ord(matrix[new_row][new_col]))
        if can_move_to_square(current_square, next_square, visited):
            next_squares.append(next_square)

    return next_squares


def can_move_to_square(current_square: Square, next_square: Square, visited: Set[Tuple[int, int]]) -> bool:
    height_diff = next_square.height - current_square.height
    return (next_square.row, next_square.col) not in visited and height_diff < 2


def out_of_bounds(row: int, col: int, matrix: Matrix) -> bool:
    return row < 0 or row == len(matrix) or col < 0 or col == len(matrix[0])


print(solve_part1(deepcopy(lines)) == 520)
print(solve_part2(deepcopy(lines)) == 508)
