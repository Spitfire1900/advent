import os
import pathlib
import sys
import textwrap

TEST_INPUT = textwrap.dedent('''\
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    ''')
INPUT = (pathlib.Path(os.path.dirname(__file__)) / 'input.txt').read_text()
PART_ONE_TEST_ANSWER = 35
PART_TWO_TEST_ANSWER = 16


def get_seeds(input: str) -> list[int]:
    return [
        int(item)
        for item in input.split('\n')[0].split(':')[1].strip().split(' ')
    ]


def get_maps(input: str):
    blocks = [item.strip() for item in input.split('\n\n')[1:]]
    return blocks


def part_one(input):
    seeds = get_seeds(input)
    maps = get_maps(input)
    ...


def part_two(input):
    ...


def main():
    print('===Part One===')
    print('Test Answer:', PART_ONE_TEST_ANSWER)
    print('Answer:', part_one(TEST_INPUT))

    print()
    print('===Part Two===')
    print('Test Answer:', PART_TWO_TEST_ANSWER)
    print('Answer:', part_two(TEST_INPUT))


if __name__ == '__main__':
    sys.exit(main())
