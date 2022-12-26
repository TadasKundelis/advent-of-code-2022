import re
from typing import List, Tuple
from instructions import instructions

Matrix = List[List[str]]
SIDE_LENGTH = 50
DIRECTIONS = ["RIGHT", "DOWN", "LEFT", "TOP"]

# row offset and column offset of each side
side_offsets = [
    (0, 50),
    (0, 100),
    (100, 50),
    (100, 0),
    (150, 0),
    (50, 50),
]


def build_matrix(input: List[str]) -> Matrix:
    max_row_length = max([len(row) for row in input])
    matrix = [[' '] * max_row_length for _ in range(len(input))]

    for row_index, row in enumerate(input):
        for col_index, char in enumerate(row):
            matrix[row_index][col_index] = char

    return matrix


# Example: '"RIGHT": lambda row, col: (1, "RIGHT", row, 0)'
# when side index 0 crosses right boundary, it goes to side no. 1, has 'RIGHT' direction
move_to_another_side = [
    {
        "RIGHT": lambda row, col: (1, "RIGHT", row, 0),
        "LEFT": lambda row, col: (3, "RIGHT", SIDE_LENGTH - row - 1, 0),
        "TOP": lambda row, col: (4, "RIGHT", col, 0),
        "DOWN": lambda row, col: (5, "DOWN", 0, col)
    },
    {
        "RIGHT": lambda row, col: (2, "LEFT", SIDE_LENGTH - row - 1, SIDE_LENGTH - 1),
        "LEFT": lambda row, col: (0, "LEFT", row, SIDE_LENGTH - 1),
        "TOP": lambda row, col: (4, "TOP", SIDE_LENGTH - 1, col),
        "DOWN": lambda row, col: (5, "LEFT", col, SIDE_LENGTH - 1)
    },
    {
        "RIGHT": lambda row, col: (1, "LEFT", SIDE_LENGTH - row - 1, SIDE_LENGTH - 1),
        "LEFT": lambda row, col: (3, "LEFT", row, SIDE_LENGTH - 1),
        "TOP": lambda row, col: (5, "TOP", SIDE_LENGTH - 1, col),
        "DOWN": lambda row, col: (4, "LEFT", col, SIDE_LENGTH - 1)
    },
    {
        "RIGHT": lambda row, col: (2, "RIGHT", row, 0),
        "LEFT": lambda row, col: (0, "RIGHT", SIDE_LENGTH - row - 1, 0),
        "TOP": lambda row, col: (5, "RIGHT", col, 0),
        "DOWN": lambda row, col: (4, "DOWN", 0, col)
    },
    {
        "RIGHT": lambda row, col: (2, "TOP", SIDE_LENGTH - 1, row),
        "LEFT": lambda row, col: (0, "DOWN", 0, row),
        "TOP": lambda row, col: (3, "TOP", SIDE_LENGTH - 1, col),
        "DOWN": lambda row, col: (1, "DOWN", 0, col)
    },
    {
        "RIGHT": lambda row, col: (1, "TOP", SIDE_LENGTH - 1, row),
        "LEFT": lambda row, col: (3, "DOWN", 0, row),
        "TOP": lambda row, col: (0, "TOP", SIDE_LENGTH - 1, col),
        "DOWN": lambda row, col: (2, "DOWN", 0, col)
    },
]


def find_right_neighbour(row: int, col: int, side_idx: int, direction: str) -> Tuple[int, str, int, int]:
    next_col = col + 1
    if next_col == SIDE_LENGTH:
        return find_position_on_another_side(row, col, side_idx, direction)
    else:
        return side_idx, direction, row, next_col


def find_left_neighbour(row: int, col: int, side_idx: int, direction: str) -> Tuple[int, str, int, int]:
    next_col = col - 1
    if next_col == -1:
        return find_position_on_another_side(row, col, side_idx, direction)
    else:
        return side_idx, direction, row, next_col


def find_top_neighbour(row: int, col: int, side_idx: int, direction: str) -> Tuple[int, str, int, int]:
    next_row = row - 1
    if next_row == -1:
        return find_position_on_another_side(row, col, side_idx, direction)
    else:
        return side_idx, direction, next_row, col


def find_bottom_neighbour(row: int, col: int, side_idx: int, direction: str) -> Tuple[int, str, int, int]:
    next_row = row + 1
    if next_row == SIDE_LENGTH:
        return find_position_on_another_side(row, col, side_idx, direction)
    else:
        return side_idx, direction, next_row, col


find_neighbour_fns = {
    "RIGHT": find_right_neighbour,
    "LEFT": find_left_neighbour,
    "TOP": find_top_neighbour,
    "DOWN": find_bottom_neighbour
}


def find_position_on_another_side(row: int, col: int, side_idx: int, direction: str) -> Tuple[int, str, int, int]:
    return move_to_another_side[side_idx][direction](row, col)


def find_next_direction(current_direction: str, change: str):
    current_direction_idx = DIRECTIONS.index(current_direction)
    next_direction_idx = current_direction_idx + 1 if change == "R" else current_direction_idx - 1 + 4
    return DIRECTIONS[next_direction_idx % 4]


def traverse(side_idx: int, coords: Tuple[int, int], instructions: List[str], direction: str, sides: List[Matrix]):
    instructions.reverse()

    while len(instructions):
        next_instruction = instructions.pop()

        if next_instruction.isdigit():
            next_instruction = int(next_instruction)
            current_row, current_col = coords

            for _ in range(next_instruction):
                new_matrix_idx, new_direction, next_row, next_col = (
                    find_neighbour_fns[direction](current_row, current_col, side_idx, direction)
                )
                if sides[new_matrix_idx][next_row][next_col] != "#":
                    current_row, current_col = next_row, next_col
                    side_idx = new_matrix_idx
                    direction = new_direction
                else:
                    break

            coords = current_row, current_col

        else:
            direction = find_next_direction(direction, next_instruction)

    return coords, direction, side_idx


def extract_cube_side(row_offset: int, col_offset: int, full_matrix: Matrix) -> Matrix:
    rows = full_matrix[row_offset:row_offset + SIDE_LENGTH]
    return [row[col_offset:col_offset + SIDE_LENGTH] for row in rows]


def solve(input: List[str], instructions: List[str]) -> int:
    matrix = build_matrix(input)
    sides = [extract_cube_side(row_offset, col_offset, matrix) for row_offset, col_offset in side_offsets]
    final_coords, final_direction, final_side_idx = traverse(0, (0, 0), instructions, "RIGHT", sides)
    return calculate_result(final_coords, final_side_idx, final_direction)


def calculate_result(coords: Tuple[int, int], side_idx: int, direction: str) -> int:
    row, col = coords
    row_offset = side_offsets[side_idx][0]
    col_offset = side_offsets[side_idx][1]
    return (row + row_offset + 1) * 1000 + (col + col_offset + 1) * 4 + DIRECTIONS.index(direction)


with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    parsed_instructions = re.findall(r'([0-9]+|[LR])', instructions)
    print(solve(lines, parsed_instructions) == 162038)  # works only for my input :(
