import re
from typing import List, Callable


def process_input_line(line: str) -> List[int]:
    nums = re.findall(r'\d+', line)
    return [int(n) for n in nums]


def condition_part1(line: List[int]) -> bool:
    a, b, c, d = line
    return (a <= c and b >= d) or (c <= a and d >= b)


def condition_part2(line: List[int]) -> bool:
    a, b, c, d = line
    return c <= b and a <= d


def solve_part1(lines: List[List[int]]) -> int:
    return len(list(filter(condition_part1, lines)))


def solve_part2(lines: List[List[int]]) -> int:
    return len(list(filter(condition_part2, lines)))


with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [process_input_line(l) for l in lines]

    print(solve_part1(lines) == 582)
    print(solve_part2(lines) == 893)
