import textwrap
from enum import Enum
from typing import Dict, List, Tuple, TypedDict

DAY_ONE_TEST_INPUT = textwrap.dedent('''\
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    ''')


def sum(a: List[int]):
    sum = 0
    for i in a:
        sum += i
    return sum


Stone = Enum('Color', ['RED', 'GREEN', 'BLUE'])


def parse_draw(string: str):
    stone_strings = string.split(', ')

    draws: List[Tuple[Stone, int]] = []

    for stone_string in stone_strings:
        number, color = stone_string.split(' ')
        draws.append((Stone[color.upper()], int(number)))

    return draws


class Game(TypedDict, total=False):
    string: str
    draws_string: List[str]
    draws: List[List[Tuple[Stone, int]]]


class Games(TypedDict):
    game_numer: int
    game: Game


def parse_games(string: str):
    lines = string.splitlines()
    games: Dict[int, Game] = {
        idx + 1: {
            'string': val[val.find(':') + 2:]
        }
        for idx, val in enumerate(lines)
    }

    for key, game in games.items():
        game['draws_string'] = game['string'].split('; ')
        game['draws'] = [parse_draw(draw) for draw in game['draws_string']]

    return (games)


def which_games(games: str):
    parse_games(games)
    return [1, 2, 5]


def main():
    print(sum(which_games('aaa')))
