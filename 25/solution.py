from copy import deepcopy
from functools import reduce
from typing import List, Tuple

DECIMAL_TO_SNAFU_MAPPING = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2"
}


def snafu_to_decimal(num: List[int]) -> int:
    num = deepcopy(num)
    x = 1

    converted = 0

    while num:
        current = num.pop()
        if current == "=":
            converted += (-2 * x)
        elif current == "-":
            converted += (-1 * x)
        else:
            converted += int(current) * x

        x *= 5

    return converted


def create_powers_of_five_list(dec_num: int) -> List[Tuple[int, int]]:
    num_of_fives = dec_num / 5
    x = 1
    idx = 0
    lst = [(0, 0)]  # 1x, 2x

    while lst[idx][1] < num_of_fives:
        lst.append((x, x * 2))
        idx += 1
        x *= 5

    return lst


def convert_to_snafu(powers_of_five: List[Tuple[int, int]], decimal_rest: int, res=[]) -> List[int]:
    if decimal_rest == 0:
        return res + [0] * len(powers_of_five)

    if decimal_rest > 0:
        one_x, two_x = powers_of_five.pop()
        sum_of_previous = sum([two_x for one_x, two_x in powers_of_five])

        if sum_of_previous * 5 >= decimal_rest:
            return convert_to_snafu(powers_of_five, decimal_rest, res + [0])
        elif one_x * 5 + sum_of_previous * 5 >= decimal_rest:
            return convert_to_snafu(powers_of_five, decimal_rest - one_x * 5, res + [1])
        else:
            return convert_to_snafu(powers_of_five, decimal_rest - two_x * 5, res + [2])

    elif decimal_rest < 0:
        one_x, two_x = powers_of_five.pop()
        sum_of_previous = sum([two_x for one_x, two_x in powers_of_five])

        if sum_of_previous * 5 >= abs(decimal_rest):
            return convert_to_snafu(powers_of_five, decimal_rest, res + [0])
        elif one_x * 5 + sum_of_previous * 5 >= abs(decimal_rest):
            return convert_to_snafu(powers_of_five, decimal_rest + one_x * 5, res + [-1])
        else:
            return convert_to_snafu(powers_of_five, decimal_rest + two_x * 5, res + [-2])


def decimal_to_snafu(dec_num: int) -> str:
    remainder = dec_num % 5
    adjustment = remainder

    if remainder < 3:
        dec_num -= remainder
    elif remainder >= 3:
        dec_num += (5 - remainder)
        adjustment = (5 - remainder) * -1

    d = [0, 1, 2]

    powers_of_five = create_powers_of_five_list(dec_num)
    snafu = convert_to_snafu(powers_of_five, dec_num)

    last_number = d[adjustment] if adjustment >= 0 else d[abs(adjustment)]
    snafu = snafu[:-1] + [last_number]

    return ''.join([DECIMAL_TO_SNAFU_MAPPING[key] for key in snafu])


def solve(snafu_nums: List[list[str]]) -> str:
    decimal_sum = reduce(lambda acc, curr: acc + snafu_to_decimal(curr), snafu_nums, 0)
    return decimal_to_snafu(decimal_sum)


with open('input.txt') as file:
    lines = [list(line.strip()) for line in file.readlines()]
    print(solve(lines) == '2-212-2---=00-1--102')
