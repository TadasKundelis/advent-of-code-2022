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
    start_row, start_col = find_start(matrix)
    end_row, end_col = find_end(matrix)

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


def find_next_squares(current_state: Square, matrix: Matrix, visited: Set[Tuple[int, int]]) -> List[Square]:
    row_modifier = [-1, 0, 1, 0]
    col_modifier = [0, 1, 0, -1]

    next_squares = []

    for i in range(4):
        new_row = current_state.row + row_modifier[i]
        new_col = current_state.col + col_modifier[i]

        if new_row < 0 or new_row == len(matrix) or new_col < 0 or new_col == len(matrix[0]):
            continue

        next_square_height = ord(matrix[new_row][new_col])

        if (new_row, new_col) not in visited and next_square_height - current_state.height < 2:
            next_squares.append(Square(new_row, new_col, next_square_height))

    return next_squares



def find_starts(matrix: List[List[str]]) -> List[Tuple[int, int]]:
    starts = []
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] == 'S' or matrix[row][col] == 'a':
                starts.append((row, col))
    return starts


def find_start(matrix: List[List[str]]) -> Tuple[int, int]:
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] == 'S':
                return row, col


def find_end(matrix: List[List[str]]) -> Tuple[int, int]:
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row]):
            if matrix[row][col] == 'E':
                return row, col


print(solve_part1(lines))
# print(solve_part2(lines))
