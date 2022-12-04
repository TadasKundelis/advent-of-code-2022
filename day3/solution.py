from typing import List, Set

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [l.strip() for l in lines]

    lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = f" {lower_case_letters}{lower_case_letters.upper()}"


    def _common_char_in_sets(*s: Set[str]) -> str:
        (char,) = set.intersection(*s)
        return char


    def find_common_char_in_line_halves(line: str) -> str:
        mid = len(line) // 2
        return _common_char_in_sets(set(line[:mid]), set(line[mid:]))


    def solve_part1() -> int:
        return sum(map(letters.index, map(find_common_char_in_line_halves, lines)))


    def chunks() -> List[List[str]]:
        return [lines[i:i + 3] for i in range(0, len(lines), 3)]


    def find_common_char_in_chunk(chunk: List[str]) -> str:
        return _common_char_in_sets(*map(set, chunk))


    def solve_part2() -> int:
        return sum(map(letters.index, map(find_common_char_in_chunk, chunks())))


    print(solve_part1() == 7875)
    print(solve_part2() == 2479)
