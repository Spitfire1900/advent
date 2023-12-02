import re
import textwrap
from typing import Generator

DAY_ONE_INPUT = textwrap.dedent('''\
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    ''')
DAY_ONE_SUM = 142

DAY_TWO_INPUT = textwrap.dedent('''\
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    oneight
    nineight
    ''')
DAY_TWO_SUM = 397

DAY = 'ONE'

INPUT = DAY_ONE_INPUT if DAY == 'ONE' else DAY_TWO_INPUT
SUM = DAY_ONE_SUM if DAY == 'ONE' else DAY_TWO_SUM


def named_number_to_int(str):
    return int(str) if str.isdigit() else {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }[str]


def line_generator(str) -> Generator[str, None, None]:
    return (line for line in str.splitlines())


def first_and_last_digit(line: str):
    if DAY == 'ONE':
        pattern = re.compile(r'\d')
    else:
        pattern = re.compile(
            r'(\d|one|two|three|four|five|six|seven|eight|nine)')
    digits = pattern.findall(line)
    return int(digits[0]), int(digits[-1])


def concat(a, b):
    return f'{a}{b}'


def add(a, b):
    return a + b


def main():
    lines = line_generator(INPUT)
    digits = (first_and_last_digit(line) for line in lines)
    concats = (concat(*digits) for digits in digits)

    sum = 0
    for var in concats:
        sum = add(sum, int(var))
    print(sum)
    assert sum == SUM
