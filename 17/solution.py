from typing import Tuple, List, Set

Rock = List[Tuple[int, int]]
Chamber = Set[Tuple[int, int]]


def rock1(row: int, col: int) -> Rock:
    return [(row, col) for col in range(col, col + 4)]


def rock2(row: int, col: int) -> Rock:
    return [(row - 1, col), (row - 1, col + 1), (row - 1, col + 2), (row, col + 1), (row - 2, col + 1)]


def rock3(row: int, col: int) -> Rock:
    return [(row, col), (row, col + 1), (row, col + 2), (row - 1, col + 2), (row - 2, col + 2)]


def rock4(row: int, col: int) -> Rock:
    return [(row, col) for row in range(row, row - 4, -1)]


def rock5(row: int, col: int) -> Rock:
    return [(row, col), (row, col + 1), (row - 1, col), (row - 1, col + 1)]


rock_builders = [rock1, rock2, rock3, rock4, rock5]


def move_to_left(rock: Rock) -> Rock:
    return [(row, col - 1) for row, col in rock]


def move_to_right(rock: Rock) -> Rock:
    return [(row, col + 1) for row, col in rock]


def move_down(rock: Rock) -> Rock:
    return [(row + 1, col) for row, col in rock]


def resolve_top_row(chamber: Chamber) -> int:
    if len(chamber) == 0:
        return 0
    elif len(chamber) == 1:
        (row,) = chamber
        return row
    else:
        return min(row for row, _ in chamber)


def solve_part1():
    start_col = 2
    chamber = set()

    for i in range(2022):
        rock_builder = rock_builders[i % len(rock_builders)]
        start_row = resolve_top_row(chamber) - 4
        rock = rock_builder(start_row, start_col)
        put_rock_into_chamber(rock, chamber)

    return resolve_top_row(chamber) * -1 + 1


def put_rock_into_chamber(rock: Rock, chamber: Chamber) -> None:
    new_rock_position = move_rock(rock, chamber)

    for row, col in new_rock_position:
        chamber.add((row, col))


global jet_pattern
jet_pattern_index = 0


def move_rock(rock: Rock, chamber: Chamber, index: int = 0):
    global jet_pattern_index

    if on_the_bottom(rock):
        return rock

    if index % 2 == 0:
        jet_move = jet_pattern[jet_pattern_index % len(jet_pattern)]
        if jet_move == '<':
            new_rock_position = move_to_left(rock)
            if blocked_by_another_rock(new_rock_position, chamber) or out_of_bounds(new_rock_position):
                jet_pattern_index += 1
                return move_rock(rock, chamber, index + 1)
            else:
                jet_pattern_index += 1
                return move_rock(new_rock_position, chamber, index + 1)

        elif jet_move == '>':
            new_rock_position = move_to_right(rock)
            if out_of_bounds(new_rock_position) or blocked_by_another_rock(new_rock_position, chamber):
                jet_pattern_index += 1
                return move_rock(rock, chamber, index + 1)
            else:
                jet_pattern_index += 1
                return move_rock(new_rock_position, chamber, index + 1)
    else:
        new_rock_position = move_down(rock)
        if blocked_by_another_rock(new_rock_position, chamber):
            return rock
        else:
            return move_rock(new_rock_position, chamber, index + 1)


def out_of_bounds(rock: Rock) -> bool:
    return any(col < 0 or col > 6 for _, col in rock)


def on_the_bottom(rock: Rock) -> bool:
    return any(row == 0 for row, _ in rock)


def blocked_by_another_rock(rock: Rock, chamber: Chamber) -> bool:
    return any((row, col) in chamber for row, col in rock)


with open('input.txt') as file:
    jet_pattern = file.readline()
    print(solve_part1() == 3067)
