import re
import sys
import textwrap
from dataclasses import dataclass
from typing import Any, Generator, List, Tuple

TEST_INPUT_DATA = textwrap.dedent('''\
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    ''')
TEST_INPUT_SUM = 4361


@dataclass
class Part():
    number: int
    row: int
    col_start: int
    col_end: int

    def __init__(self, number: int, row: int, col_start: int, col_end: int):
        self.number = number
        self.row = row
        self.col_start = col_start
        self.col_end = col_end


def symbol_locations(input_str: str) -> Generator[Tuple[int, int], Any, None]:
    print('hello')
    for row_idex, row in enumerate(input_str.splitlines()):
        for col_index, char in enumerate(row):
            if char in ['*', '#', '$']:
                yield row_idex, col_index


def probable_parts(input_str: str) -> Generator[Part, Any, None]:
    pattern = re.compile(r'(\d+)')
    for row_idex, row in enumerate(input_str.splitlines()):
        probable_matches = pattern.finditer(row)
        for probable_match in probable_matches:
            yield Part(
                number=int(probable_match.group(0)),
                row=row_idex,
                col_start=probable_match.start(),
                col_end=probable_match.end() - 1,
            )


def main():
    # print(list(symbol_locations(TEST_INPUT_DATA)))
    print(list(probable_parts(TEST_INPUT_DATA)))


if __name__ == "__main__":
    sys.exit(main())
