from typing import List, Set, Tuple, Callable

Line = List[List[int]]


def parse_line(line: str) -> Line:
    coords = line.strip().split('->')
    return [list(map(int, coord.split(','))) for coord in coords]


def solve_part1(input: List[Line]):
    cave, initial_rock_count, lowest_point = init_cave(input)
    sand_should_stop = lambda y: y + 1 > lowest_point

    while resolve_next_sand_position(cave, (500, 0), sand_should_stop)[1] < lowest_point:
        pass

    return len(cave) - initial_rock_count - 1  # -1 one for the last sand item


def solve_part2(input: List[Line]):
    cave, initial_rock_count, lowest_point = init_cave(input)
    sand_should_stop = lambda y: y + 1 == lowest_point + 2

    while resolve_next_sand_position(cave, (500, 0), sand_should_stop) != (500, 0):
        pass

    return len(cave) - initial_rock_count


def init_cave(input: List[Line]):
    cave = add_stones(input)
    initial_rock_count = len(cave)
    lowest_point = find_lowest_point(cave)
    return cave, initial_rock_count, lowest_point


def resolve_next_sand_position(
        cave: Set[Tuple[int, int]],
        current_position: Tuple[int, int],
        sand_should_stop: Callable[[int], bool]
):
    x, y = current_position

    if sand_should_stop(y):
        cave.add(current_position)
        return current_position

    lower = (x, y + 1)
    left = (x - 1, y + 1)
    right = (x + 1, y + 1)

    if lower not in cave:
        return resolve_next_sand_position(cave, lower, sand_should_stop)
    if left not in cave:
        return resolve_next_sand_position(cave, left, sand_should_stop)
    if right not in cave:
        return resolve_next_sand_position(cave, right, sand_should_stop)

    cave.add(current_position)
    return current_position


def find_lowest_point(stones):
    return sorted(list(stones), key=lambda x: x[1], reverse=True)[0][1]


def add_stones(input: List[Line]):
    stones = set()
    for line in input:
        for i in range(len(line) - 1):
            coords1, coords2 = line[i], line[i + 1]
            x1, y1 = coords1
            x2, y2 = coords2

            if x1 != x2:
                new_stones = set((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
                stones = stones.union(new_stones)

            if y1 != y2:
                new_stones = set((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
                stones = stones.union(new_stones)

    return stones


with open('input.txt', 'r') as file:
    lines = [parse_line(line) for line in file.readlines()]

    print(solve_part1(lines) == 817)
    print(solve_part2(lines) == 23416)
