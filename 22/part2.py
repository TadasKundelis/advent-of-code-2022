import re
from typing import List, Tuple

instructions = "7L36R16L35R32R7R49L24R37R5L48L43L40R40L43L7R50R47L11R50L41L41R24L50L44R4L39R30L31R36R21R48R40L26R10L6L50R39R26R37L10R44R40L36R25L39R23R46R3R18R50L48R28R10R13R17L19R1L25L1L50L17R3R41R9R40R40L26L33L27L32L49R25R40L22R32R21R14L30L34L15L29R17L18L16L49L12R8R23L20L6L1R17L45L16R45L11R2L40L15R39L6L34L2R31R12L47R27R42L34R45L38R47R5L33L50L21R28R30R34L14R37R13R11R22L41R30L26L17R25R18L45R2R49L7R31R31R7R33R43R34R41L26R40R16L39R2L43R41L46R44L31R20R37R18L22R34R39R17L23R9L24L4L11L24R5L28R29R47L14R42L47R49R35R48R3L28R8L29R29R10L23R1L32L10R30R27L11R33R30R45L23R23L32R32R3L37L38R45L26L41R33L37L30R32L24R30R9L40L47R44L7L14L48R39L49R23L30L35L19L6L17L16R47R11R33L18L50R27L44R44R30L2L16L39L50L23R37R46R46R17L40R49R33R22R50L14R26L11L50L46R9R1R34R25R4R10L9L10R16R16L18R37R33R47L12L5R37L22L46R34L19L12R17L15L35L25L25L44L42R47L2L6R22L48L27L34R50R24R45R46L22L16L37R10R22L31R26L16L13R10R5L21L18R7R23L3R31L40L21R13L39L37R17L41R2L42R47R1R16L25L50R27L16R30R12R37R12R22R45L25L18R43R3R20R1L14L41L37R11L29R47L38R2L8L22R22R34R36L8L26R48L7L41R49L17R34L42R49L35L40R25R20R3L50R18L23R36L41R30L49L35R25L35R49L11R45R34R25L41R50L50R10L49L11L35L5R14L5L35L23L45R50L32L50R41R45R1L18L7R17L31L31L39R26R19R31R47L50R13R18R45R39L27R25R4L3L8R39L34L24L48R28L32R32L11L14R37L7R5L20R38R36L23L47R8R46R26R30R18R8R30R4R43L24R45R48L45R28L16R20L15R32L27L39R3L49L4L6R12L12L40L3R20R5L8R17R8L35R24R18L38L21L46L24L42R40L19L2L45L12L25L27L1L5R20L10L20L36L37L33R46L42R33L6L6L12L43R5R32R5R44L24R32L45L2L30R8R41L45R20L16R34L8L46R35L40R47L6R7L49L19L37L32L41L4R47L20R2L42R20R7L23R5R27R39L1R25L15L28L19L26L11L21L16L4R29R35R50L34L8R13L27L49L34R43R44R1R46L24R18L46R36L19L14R2R10R38L40L45L4R32R37L17R44R4R9R31R15L10R27L9L17L44L17L46L11L14L16L2R20L50R50R39L17R39L29R11L26L33R26R25R15R32L24R34L44R22L11L29L15L8L12R13R33L50L10R27L45R34L1L25R30L44R7R47L9R27L22R6L29L48R26R1L23L19L32R17L50L1L32L44L10R13R32R22R39R31R39R9R21L50R37R4L47R25R34R31L41L34L42L33L18L38L18R36L46R26L2L15L32R43R31L44R10L11L48R25R49L4R43R20R22R34L31L27R26L1L14R5R47L24L39L3R38L12R8L40L36L49R3L30L30R7R8R35L24L18L14R29R19L28L40R21L33L16L47R32R50L2L9R13R34R12R28R44L50L18L10R47L34L36L20L17L44R44R20R44L47L18L1L13R21R50R13R42R46R27L7L25R28R25R32L15L32L3R17L15L9L37R39R6L43R37R17R9R46R48R45L14R6R15L30R49R30L4R12L28L42L48R6R50L9L40R24R38R43R2L4L36R7L48R20R38L5R12L49R46L45L19L17R11L19L48R22R39R21L29L13L3L25L35L34R26L10R7L40L43L7L40R23R28L29L46R49L1R47R4R2R16L25R39L27L47L16L19L7R10L28L47L44R41R23R45R18L49R7R14L5R49L29L1R18R13R19R29L31L19L39R32L33L15L38R8R26R7R27R31R48R23L24L8R21R4L48R30L22L5R30L13R28L21L23L19R17L32L9R45L19L26L8L34L27L10R14L47R49L50R25R41L24R44L49L35R47R35R28R42R10R42L35L34R26L23L12L39R25R24R11L1R18L17L24R28L20L25R26R9R46R10L38L24L29R28R15L49L23R24R35L48R21R6L26L47L21R30R46L34L28R13L25R36L9R18L41L41L27L32L30L6L32R22R18L49R34R20L13L42L26L29R44L16L7L47L44L1R37R6L27R44R10L10R2L6R22R16L4L40R39L8R6R45R44L2L29R20R5R6L38R21L42L10R38R3R37L23L20L14L14R42L4L14R30R35L28L32R34L45L19L35L30L1L14L31R10R41R42R29R43R41L24R9L15L29L39R9L8L31L41L29R40R7R23R8R18R37R12L7L26L48R32R37L25L15L21L27L37L14R44R17R30R30L46L12R12R12L43R50L18L41L23L37L37L11L43L27R22L37R43L21R43R38L25R33R33R49R29R32L1L48L12L5R37R25R24L1L46L18L19L33R12L46L50L4L17R33L16R46L31R35L8R45R35R31R21L25L43L7R18L18L13L8R45L29R1R36R5L48L9L29L24L2R24R25R29R19R43R8R25L4R49R18R19L29L41R34R2R24R29R11L13L30R34R38L12L48R6R50L42R31L29L44R25L41R47L19L4L49L7L29L40L16R41L42L9R9R50R4R45R17L20R39L43L48L11R20L10R2R34L15L46R1R23L43L39R42R6L13L26L8R25R12R31L44R33L23R33L34R18L13R9R35L34R12R32L15R25R47L41L43L23L39R47L12L29R7L34L36R46R41L2L40L31R19L48R28R31R38R36L46L46R24R45L44L20L5R43R25R47L49R40R25R41L47R15L8L37R8L38L36R33L48R39L11R49L50R12R33R48L40R37R31L27R39L16R41L14L10L32L19L9R45L24R3L20L3R49R31L42R1L17L40R20R8L11R18R17L41R16L10L48L38R15L28R47L48L24L18R15L23R22L3R40L46R4R49R6R43L24R34L3L42L10R50L19R22R36R7L28R33L41L10L47R33L17R48L8R49L10R34R9R33L36R21R10R24R4L30R14L25R1R10L20R3R33R3R41L6L14L4R31L42R39L25R32R26L26R13R4R25R3L49R20L27L39R44L38R49R47L46R9L33R4R33L18R14R36L12L47R14R29R12L48L1R16R26R37R30L39R3R17L40L45L31R12R16L50R19L18R31R50R33R34L3R1L15L49L9L35R22R12L3R14R13L50R11L41L28L39L50L9L14L21L36L20L8L13R4L10R32R46L29L37L27R10L5R6L16R1L35R42R27R48R28R27R42L46L4R9R9R8R19R1R28R50R9L47L46R45R43L14R37L21R17R6R40L46L40R40L29L26R26R20L50L47L37L37L17L39L22R19L39R23R7R9R6L30L31R35R37R17R33L9R38R1R24R19R3L15L47L3L14R21L42R46L39L27R35R32L31L37R49R17R31L7L30R35R26R21R45L8L46L35R38R1L44R26L19L44L12R34R28R11L8R34L12R33L15L48L7R28L11L31R20R47R48L9R33L34L47L21R19L27L22R21R24R24R32R50L29R16R50R13L31R42L39R22R45R17R48R38R7L47R38R38L32R18L22L17L28R12L35L38L13R44L21L42L46R22R19R39R1R12L8R20L43R2R2L22R9R13L30L31R8L8L27R48R16L30L37R19L45R3R39L16L7R50R47R10R9L50L1R27L38R31R27L46R5L43L3R47L9L20R23R15R12L26R19L46R32L18R29R33L50R39L46L31R45L47L45L33L32R25R7R39R43R41L48L46L28R3L13L26L41L50R10R50L26R26L43L32R16R2R39L50R23R49L39L45L39R31R16L41L31L1R9R26R27L45L31R36R32R2L29L21L47R18L16R41R48L22R33L16L48L5R37L36L46R11R17R26R33L32R40R11R13L48L45L7L30R43R28L49R38R6R11L50R45L37L34L28R19R4L7L18R22L30L4R1L7R20L30L27L35L23R12L19R30L1R12R33L1R25R22R15L30L47R15L23L7R30R24R33R34L42R13L35R41R50R27L24R16R16R31R26L10L40R41R41L49L18R14R1R44L12R33R37R25R9R1R42R14R14L10R29R15R47R40R16R12R14R11L48L32L30R30L39L31R8L13R26L34R46L25R47L26R19R29R48R8R30L49R12R13L25L7L12R50R49L28L1R16L8R44R33R1R33R18L31R48R42L13R25R34R7R13L32R46L27R3L15R28L10L35R17R38R29L40L40R44L37L8R29R31R39R36L22R16R11L5R50R17R46L9R42R48L46R31R11R20L14R16L13L8R37R24R5R2L27R48L33R27R10R43L47R19L21L10L21L21L36R13L20L41L38L7R31R33L31R16L43L23L6R45R13L14R20L23L39R38R34L32R41R31L41L34R40R33R29L14L36R2L15R38L44R26R28L8R27R44R33R1L35R46R32L49L24R42R38R48R6R15L15L22L12R30L2R39R21R23R16R37L36L14R42R23L26R45R11L33L18R21L50R41R33R21R1R47L11L14L3L2L45R8L37L14L37R34R6R8L30"

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
    print(solve(lines, parsed_instructions) == 162038) # works only for my input :(
