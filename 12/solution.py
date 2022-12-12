import heapq
from dataclasses import dataclass
from typing import List, Tuple, Set
from collections import namedtuple

with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

    letters = 'abcdefghijklmnopqrstuvwxyz'

# def solve_part2(matrix: List[List[str]]) -> int:
#     res = []
#     for start_row, start_col in find_starts(matrix):
#         possible_start_squares = find_next_states(start_row, start_col, matrix, set())
#         start_squares = []
#
#         for p_row, p_col in possible_start_squares:
#             if letters.index(matrix[p_row][p_col]) - letters.index(matrix[start_row][start_col]) > 1:
#                 continue
#             else:
#                 start_squares.append((p_row, p_col))
#         # print(start_squares)
#
#         heap = []
#         visited = set()
#
#         for square in start_squares:
#             visited.add(square)
#             heapq.heappush(heap, (1, square))
#
#         while len(heap) > 0:
#             current = heapq.heappop(heap)
#             # print("current")
#             # print(current)
#             cost = current[0]
#             row, col = current[1]
#
#             next_squares = find_next_states(row, col, matrix, visited)
#             # print("next squares")
#             # print(next_squares)
#
#             for next_square_row, next_square_col in next_squares:
#                 next_square = matrix[next_square_row][next_square_col]
#                 if next_square == 'E' and (matrix[row][col] == 'z' or matrix[row][col] == 'y'):
#                     res.append(cost + 1)
#                 elif letters.index(next_square) - letters.index(matrix[row][col]) > 1:
#                     continue
#                 else:
#                     visited.add((next_square_row, next_square_col))
#                     heapq.heappush(heap, (cost + 1, (next_square_row, next_square_col)))
#
#     return min(res)

Square = namedtuple('State', ['row', 'col', 'height'])
Matrix = List[List[str]]

def solve_part1(matrix: Matrix) -> int:
    start_row, start_col = find_square('S', matrix)
    end_row, end_col = find_square('E', matrix)

    matrix[end_row][end_col] = 'z'

    start_square = Square(start_row, start_col, height=ord('a'))

    heap = []
    heapq.heappush(heap, (0, start_square))
    visited = {(start_row, start_col)}

    while len(heap) > 0:
        current_cost, current_state = heapq.heappop(heap)
        next_squares = find_next_squares(current_state, matrix, visited)

        for next_square in next_squares:
            if next_square.row == end_row and next_square.col == end_col:
                return current_cost + 1
            visited.add((next_square.row, next_square.col))
            heapq.heappush(heap, (current_cost + 1, next_square))


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


def find_starts(matrix: List[List[str]]) -> List[Tuple[int, int]]:
    starts = []
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] == 'S' or matrix[row][col] == 'a':
                starts.append((row, col))
    return starts

def find_square(square: str, matrix: Matrix) -> Tuple[int, int]:
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] == square:
                return row, col


print(solve_part1(lines) == 520)
# print(solve_part2(lines))
