import re
from dataclasses import dataclass
from typing import List, Tuple
from instructions import instructions

DIRECTIONS = ["RIGHT", "DOWN", "LEFT", "TOP"]


@dataclass
class Node:
    row: int
    col: int
    value: str
    left: Tuple[int, int] = None
    right: Tuple[int, int] = None
    top: Tuple[int, int] = None
    bottom: Tuple[int, int] = None


Matrix = List[List[str]]
NodeMatrix = List[List[Node]]


def build_matrix(input: List[str]):
    max_row_length = max([len(row) for row in input])
    matrix = [[' '] * max_row_length for _ in range(len(input))]

    for row_index, row in enumerate(input):
        for col_index, char in enumerate(row):
            matrix[row_index][col_index] = char

    return matrix


def build_nodes(matrix: Matrix) -> NodeMatrix:
    node_matrix = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            node_matrix[row_index][col_index] = Node(row_index, col_index, value)

    return node_matrix


def add_neighbours_to_nodes(matrix: NodeMatrix) -> NodeMatrix:
    graph = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for col_index, node in enumerate(row):
            if node.value == " " or node.value == "#":
                graph[row_index][col_index] = node
            else:
                node.right = find_right_neighbour(row_index, col_index, matrix)
                node.left = find_left_neighbour(row_index, col_index, matrix)
                node.top = find_top_neighbour(row_index, col_index, matrix)
                node.bottom = find_bottom_neighbour(row_index, col_index, matrix)

            graph[row_index][col_index] = node

    return graph


def find_right_neighbour(row_index: int, col_index: int, node_matrix: NodeMatrix) -> Tuple[int, int]:
    row_length = len(node_matrix[0])
    next_col_index = (col_index + 1) % row_length
    if node_matrix[row_index][next_col_index].value != " ":
        return row_index, next_col_index
    else:
        return find_right_neighbour(row_index, next_col_index, node_matrix)


def find_left_neighbour(row_index: int, col_index: int, node_matrix: NodeMatrix) -> Tuple[int, int]:
    row_length = len(node_matrix[0])
    next_col_index = (col_index + row_length - 1) % row_length
    if node_matrix[row_index][next_col_index].value != " ":
        return row_index, next_col_index
    else:
        return find_left_neighbour(row_index, next_col_index, node_matrix)


def find_top_neighbour(row_index: int, col_index: int, node_matrix: NodeMatrix) -> Tuple[int, int]:
    col_length = len(node_matrix)
    next_row_index = (row_index + col_length - 1) % col_length
    if node_matrix[next_row_index][col_index].value != " ":
        return next_row_index, col_index
    else:
        return find_top_neighbour(next_row_index, col_index, node_matrix)


def find_bottom_neighbour(row_index: int, col_index: int, node_matrix: NodeMatrix) -> Tuple[int, int]:
    col_length = len(node_matrix)
    next_row_index = (row_index + 1) % col_length
    if node_matrix[next_row_index][col_index].value != " ":
        return next_row_index, col_index
    else:
        return find_bottom_neighbour(next_row_index, col_index, node_matrix)


def find_root(matrix: NodeMatrix) -> Tuple[int, int]:
    for row_index, row in enumerate(matrix):
        for col_index, node in enumerate(row):
            if node and node.value == ".":
                return row_index, col_index


def find_next_direction(current_direction: str, change: str):
    directions = ["UP", "RIGHT", "DOWN", "LEFT"]
    current_direction_idx = directions.index(current_direction)
    if change == "R":
        next_direction = directions[(current_direction_idx + 1) % 4]
    else:
        next_direction = directions[(current_direction_idx - 1 + 4) % 4]

    return next_direction


def traverse(node_matrix: NodeMatrix, node_coords: Tuple[int, int], instructions: List[str], direction: str):
    instructions.reverse()

    while len(instructions):
        next_instruction = instructions.pop()

        if next_instruction.isdigit():
            next_instruction = int(next_instruction)
            current_row, current_col = node_coords

            if direction == "RIGHT":
                for _ in range(next_instruction):
                    next_row, next_col = node_matrix[current_row][current_col].right
                    if node_matrix[next_row][next_col].value != "#":
                        current_row, current_col = next_row, next_col
                    else:
                        break

            if direction == "LEFT":
                for _ in range(next_instruction):
                    next_row, next_col = node_matrix[current_row][current_col].left
                    if node_matrix[next_row][next_col].value != "#":
                        current_row, current_col = next_row, next_col
                    else:
                        break

            if direction == "UP":
                for _ in range(next_instruction):
                    next_row, next_col = node_matrix[current_row][current_col].top
                    if node_matrix[next_row][next_col].value != "#":
                        current_row, current_col = next_row, next_col
                    else:
                        break

            if direction == "DOWN":
                for _ in range(next_instruction):
                    next_row, next_col = node_matrix[current_row][current_col].bottom
                    if node_matrix[next_row][next_col].value != "#":
                        current_row, current_col = next_row, next_col
                    else:
                        break

            node_coords = current_row, current_col

        else:
            direction = find_next_direction(direction, next_instruction)

    return node_coords, direction


def solve(input: List[str], instructions: List[str]) -> int:
    matrix = build_matrix(input)
    node_matrix = build_nodes(matrix)
    node_matrix = add_neighbours_to_nodes(node_matrix)
    root = find_root(node_matrix)
    final_coords, final_direction = traverse(node_matrix, root, instructions, "RIGHT")
    final_row, final_col = final_coords
    return (final_row + 1) * 1000 + (final_col + 1) * 4 + DIRECTIONS.index(final_direction)


with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    parsed_instructions = re.findall(r'([0-9]+|[LR])', instructions)
    print(solve(lines, parsed_instructions) == 106094)
