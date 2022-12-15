from typing import List


def parse_line(line: str) -> List[List[int]]:
    coords = line.strip().split('->')
    return [list(map(int, coord.split(','))) for coord in coords]


def solve_part1(lines):
    cave = add_stones(lines)
    start = (500, 0)
    sand_count = 0

    while resolve_next_sand_position(cave, start, find_lowest(cave)):
        sand_count += 1

    return sand_count


def solve_part2(lines):
    cave = add_stones(lines)
    lowest = find_lowest(cave) + 2
    sand_count = 1

    while resolve_next_sand_position2(cave, (500, 0), lowest) != (500, 0):
        sand_count += 1

    return sand_count


def resolve_next_sand_position2(cave, current_position, lowest):
    x, y = current_position

    if y + 1 == lowest:
        cave.add(current_position)
        return current_position

    lower = (x, y + 1)
    left = (x - 1, y + 1)
    right = (x + 1, y + 1)

    if lower not in cave:
        return resolve_next_sand_position2(cave, lower, lowest)
    if left not in cave:
        return resolve_next_sand_position2(cave, left, lowest)
    if right not in cave:
        return resolve_next_sand_position2(cave, right, lowest)

    cave.add(current_position)
    return current_position


def resolve_next_sand_position(cave, current_position, lowest):
    x, y = current_position

    if y + 1 > lowest:
        return False

    lower = (x, y + 1)
    left = (x - 1, y + 1)
    right = (x + 1, y + 1)

    if lower not in cave:
        return resolve_next_sand_position(cave, lower, lowest)
    if left not in cave:
        return resolve_next_sand_position(cave, left, lowest)
    if right not in cave:
        return resolve_next_sand_position(cave, right, lowest)

    cave.add(current_position)
    return True


def find_lowest(stones):
    return sorted(list(stones), key=lambda x: x[1], reverse=True)[0][1]


def add_stones(lines):
    stones = set()
    for line in lines:
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
