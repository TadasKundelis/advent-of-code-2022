from typing import List, Union, Optional, Any

Packet = List[Union[int, List['Packet']]]

with open('input.txt', 'r') as file:
    packets = [eval(line.strip()) for line in file.readlines() if line.strip() != '']

    print(solve_part1(packets) == 5720)
    print(solve_part2(packets + [[[2]], [[6]]]) == 23504)


def group_into_pairs(lines: List[List[int]]) -> List[List[List[int]]]:
    return [lines[i:(i + 2)] for i in range(0, len(lines) - 1, 2)]


def is_int(obj: Any) -> bool:
    return isinstance(obj, int)


def are_packets_in_order(left, right) -> Optional[bool]:
    right_length = len(right)
    left_length = len(left)

    iterations = max(right_length, left_length)

    for i in range(iterations):
        if i == right_length:
            return False
        elif i == left_length:
            return True

        left_elem = left[i]
        right_elem = right[i]

        if is_int(left_elem) and is_int(right_elem):
            if left_elem != right_elem:
                return left_elem < right_elem
        else:
            left_elem = [left_elem] if isinstance(left_elem, int) else left_elem
            right_elem = [right_elem] if isinstance(right_elem, int) else right_elem
            res = are_packets_in_order(left_elem, right_elem)

            if res is not None:
                return res

    return None


def sort_packets(packets: List[Packet]) -> List[Packet]:
    for i in range(len(packets) - 1):
        for j in range(len(packets) - 1):
            if not are_packets_in_order(packets[j], packets[j + 1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
    return packets


def solve_part1(packets: List[Packet]) -> int:
    packet_pairs = group_into_pairs(packets)
    indexes = [index + 1 if are_packets_in_order(*pair) else 0 for index, pair in enumerate(packet_pairs)]
    return sum(indexes)


def solve_part2(packets: List[Packet]) -> int:
    sorted_packets = sort_packets(packets)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
