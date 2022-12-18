import re
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Valve:
    name: str
    flow_rate: int
    neighbours: List[str]


def parse_line(line: str) -> Valve:
    result = re.search(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line.strip())
    valve_name, flow_rate, neighbours = result.groups()
    neighbours = [n.strip() for n in neighbours.split(',')]
    return Valve(name=valve_name, flow_rate=int(flow_rate), neighbours=neighbours)


def solve_part1(valves: List[Valve]):
    graph = {valve.name: valve for valve in valves}
    return solve((0, graph['AA'], 30, set()), graph)


cache = {}


def solve(state: Tuple[int, Valve, int, Set[str]], graph):
    released_pressure, valve, time_left, opened = state

    if time_left <= 1:
        return released_pressure

    cache_key = f"{valve.name}#{time_left}"

    if cache.get(cache_key, 0) > released_pressure:
        return 0

    cache[cache_key] = released_pressure

    neighbours = [graph[neighbour] for neighbour in valve.neighbours]
    results = [0]

    for neighbour in neighbours:
        if valve.name not in opened and valve.flow_rate > 0:
            next_released_pressure = released_pressure + valve.flow_rate * (time_left - 1)
            next_state = (next_released_pressure, neighbour, time_left - 2, opened | {valve.name})
            results.append(solve(next_state, graph))

        next_state_without_opened_valve = (released_pressure, neighbour, time_left - 1, opened)
        results.append(solve(next_state_without_opened_valve, graph))

    return max(results)


with open('input.txt', 'r') as file:
    valves = [parse_line(line) for line in file.readlines()]
    print(solve_part1(valves) == 1862)
