import os
import pathlib
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
INPUT_DATA = (pathlib.Path(os.path.realpath(__file__)).parent /
              'input.txt').read_text()


@dataclass(frozen=True)
class Part():
    number: int
    row: int
    col_start: int
    col_end: int

    # is_adjacent_to_symbol: None|bool
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
            if (self.row + 1, col) in symbol_locations:
                return True
        return False


def symbol_locations(input_str: str) -> Generator[Tuple[int, int], Any, None]:
    for row_idex, row in enumerate(input_str.splitlines()):
        for col_index, char in enumerate(row):
            if not char.isdigit() and char != '.':
                # if char in ['!', '*', '#', '$', '+']:
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


def asterisk_locations(
        input_str: str) -> Generator[Tuple[int, int], Any, None]:
    for row_idex, row in enumerate(input_str.splitlines()):
        for col_index, char in enumerate(row):
            if char == '*':
                yield row_idex, col_index


def adjacent_parts(coordinate: Tuple[int, int], parts: List[Part]):
    # previous row
    for col in range(coordinate[1] - 1, coordinate[1] + 2):
        for part in parts:
            if part.row == coordinate[0] - 1:
                if col in range(part.col_start, part.col_end + 1):
                    yield part
    # # same row
    for col in [coordinate[1] - 1, coordinate[1] + 1]:
        for part in parts:
            if part.row == coordinate[0]:
                if col in range(part.col_start, part.col_end + 1):
                    yield part
    # # next row
    for col in range(coordinate[1] - 1, coordinate[1] + 2):
        for part in parts:
            if part.row == coordinate[0] + 1:
                if col in range(part.col_start, part.col_end + 1):
                    yield part


def main():
    # print(list(symbol_locations(TEST_INPUT_DATA)))
    test_input_symbols = list(symbol_locations(TEST_INPUT_DATA))
    print('test input symbols:')
    print(test_input_symbols)
    test_input_parts_to_check = probable_parts(TEST_INPUT_DATA)
    test_input_parts = list(
        matched_parts(test_input_parts_to_check, test_input_symbols))

    print('test input parts:')
    print([part.number for part in test_input_parts])
    print(
        f'TEST_INPUT_PART_1_ANSWER: {sum([part.number for part in test_input_parts])}'
    )

    symbols = list(symbol_locations(INPUT_DATA))
    parts_to_check = probable_parts(INPUT_DATA)
    parts = list(matched_parts(parts_to_check, symbols))
    print(f'ANSWER: {sum([part.number for part in parts])}')

    test_input_asterisks = list(asterisk_locations(TEST_INPUT_DATA))
    print('test input asterisks:')
    print(test_input_asterisks)
    print(set(adjacent_parts(test_input_asterisks[0], test_input_parts)))


if __name__ == "__main__":
    sys.exit(main())
