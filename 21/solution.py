import re
from typing import Dict, Any


def parse_line(line: str):
    name, operation = line.strip().split(':')
    name, operation = name.strip(), operation.strip()

    if operation.isdigit():
        return name.strip(), operation.strip()
    else:
        operation = operation.strip().split(' ')
        return name.strip(), operation


def solve_part1(monkey: str, graph: Dict[str, Any]):
    action = graph[monkey]
    if isinstance(action, str):
        return action
    else:
        left, operation, right = action
        return eval(f"{solve_part1(left, graph)}{operation}{solve_part1(right, graph)}")


def solve_part2(monkey: str, graph: Dict[str, Any]):
    action = graph[monkey]
    if monkey == 'humn':
        return 'X'
    elif isinstance(action, str):
        return action
    else:
        left, operation, right = action
        left = solve_part2(left, graph)
        right = solve_part2(right, graph)
        result = f"{left} {operation} {right}"
        return eval(result) if 'X' not in result else f"({result})"


def get_input_for_part_2(file_contents: str) -> str:
    return re.sub(r'(root: [a-z]+) . ([a-z]+)', '\\1 = \\2', file_contents)


def create_graph(file_contents: str) -> Dict[str, Any]:
    monkeys = [parse_line(line) for line in file_contents.split('\n')]
    return {monkey_name: operation for monkey_name, operation in monkeys}


with open('input.txt') as file:
    content = file.read()
    print(solve_part1('root', create_graph(content)) == 170237589447588)

    input_part2 = get_input_for_part_2(content)
    print(solve_part2('root', create_graph(input_part2)))  # renders equation; 3712643961892
