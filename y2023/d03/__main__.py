import re
import sys
import textwrap
from dataclasses import dataclass
from typing import Any, Generator, Iterable, List, Tuple

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

    # is_adjacent_to_symbol: None|bool

    def __init__(self, number: int, row: int, col_start: int, col_end: int):
        self.number = number
        self.row = row
        self.col_start = col_start
        self.col_end = col_end

    def has_adjacent_symbols(self, symbol_locations: List[Tuple[int,
                                                                int]]) -> bool:
        # prior row
        for col in range(self.col_start - 1, self.col_end + 2):
            if (self.row - 1, col) in symbol_locations:
                return True
        # same row
        for col in [self.col_start - 1, self.col_end + 1]:
            if (self.row, col) in symbol_locations:
                return True
        # next row
        for col in range(self.col_start - 1, self.col_end + 2):
            if (self.row - +1, col) in symbol_locations:
                return True
        return False


def symbol_locations(input_str: str) -> Generator[Tuple[int, int], Any, None]:
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


def matched_parts(
    parts: Iterable[Part],
    symbol_locations: List[Tuple[int, int]],
) -> Generator[Part, Any, None]:
    for part in parts:
        if part.has_adjacent_symbols(symbol_locations):
            yield part


def main():
    # print(list(symbol_locations(TEST_INPUT_DATA)))
    symbols = list(symbol_locations(TEST_INPUT_DATA))
    print('symbols:')
    print(symbols)
    parts_to_check = probable_parts(TEST_INPUT_DATA)
    parts = matched_parts(parts_to_check, symbols)

    print('parts:')
    print([part.number for part in parts])

    # print(list(probable_parts(TEST_INPUT_DATA)))


if __name__ == "__main__":
    sys.exit(main())
