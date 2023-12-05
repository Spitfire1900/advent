from . import __main__ as main


def test_parse_cards():
    card_generator = main.parse_cards(main.PART_ONE_TEST_INPUT)
    assert card_generator.send(None) == main.Card(
        number=1,
        winning_numbers=[41, 48, 83, 86, 17],
        your_numbers=[83, 86, 6, 31, 17, 9, 48, 53],
    )
    assert card_generator.send(None) == main.Card(
        number=2,
        winning_numbers=[13, 32, 20, 16, 61],
        your_numbers=[61, 30, 68, 82, 17, 32, 24, 19],
    )


def test_part_one_card_points():
    card_generator = main.parse_cards(main.PART_ONE_TEST_INPUT)
    assert card_generator.send(None).get_points() == 8  # 1
    assert card_generator.send(None).get_points() == 2  # 2
    assert card_generator.send(None).get_points() == 2  # 3
    assert card_generator.send(None).get_points() == 1  # 4
    assert card_generator.send(None).get_points() == 0  # 5
    assert card_generator.send(None).get_points() == 0  # 6


def test_part_one_score():
    assert main.get_part_one_score(
        main.PART_ONE_TEST_INPUT) == main.PART_ONE_TEST_ANSWER
