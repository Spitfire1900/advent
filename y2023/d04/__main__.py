import os
import pathlib
import re
import sys
import textwrap
from dataclasses import dataclass
from typing import Any, Generator, List

TEST_INPUT = textwrap.dedent('''\
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    ''')
INPUT = (pathlib.Path(os.path.dirname(__file__)) / 'input.txt').read_text()
PART_ONE_TEST_ANSWER = 13
PART_TWO_TEST_ANSWER = 30


@dataclass()
class Card():
    number: int
    winning_numbers: list[int]
    your_numbers: list[int]
    matches: int = 0
    copies: int = 1

    def get_points(self) -> int:
        matches = 0
        for number in self.your_numbers:
            if number in self.winning_numbers:
                matches += 1

        score = 0
        i = 0
        while i < matches:
            if score == 0:
                score = 1
            else:
                score *= 2
            i += 1
        self.matches = matches
        return score

    # def get_part_two_copies(self, next_cards: List["Card"]):
    #     if self.matches > 0:
    #         self.copies += 1

    #     i = 0
    #     while i < self.matches:
    #         next_cards[i].copies += 1
    #         i += 1

    #     return self.copies


def parse_cards(input: str) -> Generator[Card, None, Any]:
    pattern = re.compile(r'\d+')
    lines = input.splitlines()
    for line in lines:
        card_number = int(line.split(':')[0].split(' ')[-1])
        winning_numbers = [
            int(item) for item in pattern.findall(
                line.split(':')[1].strip().split('|')[0].strip())
        ]
        your_numbers = [
            int(item) for item in pattern.findall(
                line.split(':')[1].strip().split('|')[1].strip())
        ]
        yield Card(number=card_number,
                   winning_numbers=winning_numbers,
                   your_numbers=your_numbers)


def get_part_one_score(input: str):
    cards = parse_cards(input)
    score = sum(card.get_points() for card in cards)
    return score


def get_part_two_score(input: str):
    total_scratchcards = 0
    cards = list(parse_cards(
        input))  # TODO: https://stackoverflow.com/a/1012089/2673149
    [card.get_points() for card in cards]
    for idx, card in enumerate(cards):
        total_scratchcards += card.copies
        c = 0
        while c < card.copies:
            i = 0
            while i < card.matches:
                # try:
                cards[idx + i + 1].copies += 1
                # except IndexError:
                # break
                i += 1
            c += 1
    return total_scratchcards


def main():
    print('Part 1: ', get_part_one_score(INPUT))
    print('Part 2: ', get_part_two_score(INPUT))


if __name__ == '__main__':
    sys.exit(main())
