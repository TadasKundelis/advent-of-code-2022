from typing import List, Tuple, Set

Cube = Tuple[int, int, int]


def solve_part1(cubes: List[Cube]) -> int:
    return sum([6 - count_adjacent_cubes(cube, cubes) for cube in cubes])


def solve_part2(cubes: List[Cube]) -> int:
    cubes_lookup = {(x, y, z) for x, y, z in lines}

    total_uncovered_sides = solve_part1(cubes)
    air_bubbles = set()
    bounds = find_bounds(cubes)

    for cube in cubes:
        for adjacent_cube in generate_adjacent_cubes(cube, cubes_lookup):
            is_inner_bubble, current_visited = find_inner_bubbles(adjacent_cube, cubes_lookup, bounds)
            if is_inner_bubble:
                air_bubbles |= current_visited

    internal_sides = sum([count_adjacent_cubes(bubble, cubes) for bubble in air_bubbles])
    return total_uncovered_sides - internal_sides


def find_bounds(cubes: List[Cube]) -> Tuple[int, int, int, int, int, int]:
    min_x = min(x for x, y, z in cubes)
    max_x = max(x for x, y, z in cubes)
    min_y = min(y for x, y, z in cubes)
    max_y = max(y for x, y, z in cubes)
    min_z = min(z for x, y, z in cubes)
    max_z = max(z for x, y, z in cubes)
    return min_x, max_x, min_y, max_y, min_z, max_z


def find_inner_bubbles(current_position: Cube, cubes: Set[Cube], bounds: Tuple[int, ...]) -> Tuple[bool, Set[Cube]]:
    queue = [current_position]
    min_x, max_x, min_y, max_y, min_z, max_z = bounds
    visited = set()

    while len(queue):
        air_bubble = queue.pop()
        x, y, z = air_bubble
        visited.add(air_bubble)

        if x <= min_x or x >= max_x or y <= min_y or y >= max_y or z <= min_z or z >= max_z:
            return False, visited

        for cube in generate_adjacent_cubes(air_bubble, cubes):
            if cube not in visited:
                visited.add(cube)
                queue.append(cube)

    return True, visited


def generate_adjacent_cubes(current_position: Cube, existing_cubes: Set[Cube]) -> List[Cube]:
    x, y, z = current_position
    possible_cubes = [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]
    return [cube for cube in possible_cubes if cube not in existing_cubes]


def count_adjacent_cubes(current_cube: Cube, cubes: List[Cube]) -> int:
    count = 0
    current_x, current_y, current_z = current_cube

    for adjacent_x, adjacent_y, adjacent_z in cubes:
        if abs(current_x - adjacent_x) + abs(current_y - adjacent_y) + abs(current_z - adjacent_z) == 1:
            count += 1

    return count


with open('input.txt') as file:
    lines = [line.split(',') for line in file.readlines()]
    lines = [tuple(map(int, line)) for line in lines]
    print(solve_part1(lines) == 3662)
    print(solve_part2(lines) == 2060)
