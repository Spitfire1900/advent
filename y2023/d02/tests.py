import textwrap

from impl import MaxStones, which_games


def test_which_games():
    example_input = textwrap.dedent('''\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    ''')
    PART_ONE_MAX_STONES: MaxStones = {'RED': 12, 'GREEN': 13, 'BLUE': 14}
    assert which_games(example_input, **PART_ONE_MAX_STONES) == [1, 2, 5]
