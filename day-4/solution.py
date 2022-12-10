from functools import reduce
from typing import List, Callable
import re


def process_input_line(line: str) -> List[List[int]]:
    a, b, c, d = re.findall(r'\d+', line)
    return [[int(a), int(b)], [int(c), int(d)]]


def count_overlaps(predicate: Callable[[List[int]], bool]) -> Callable[[int, List[int]], int]:
    def inner(count: int, line: List[int]) -> int:
        return count + 1 if predicate(line) else count

    return inner


def condition_part1(line: List[int]) -> bool:
    a, b, c, d = line
    return (a <= c and b >= d) or (c <= a and d >= b)


def condition_part2(line: List[int]) -> bool:
    _, b, c, _ = line
    return c <= b


def solve_part1(lines: List[List[int]]) -> int:
    return reduce(count_overlaps(condition_part1), lines, 0)


def solve_part2(lines: List[List[int]]) -> int:
    return reduce(count_overlaps(condition_part2), lines, 0)


with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [process_input_line(l) for l in lines]

    for line in lines:
        line.sort(key=lambda x: (x[0]))

    lines = [l[0] + l[1] for l in lines]

    print(solve_part1(lines) == 582)
    print(solve_part2(lines) == 893)
