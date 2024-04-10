import pytest
import board


def test_empty_board_fails():
    with pytest.raises(TypeError):
        empty_board = board.Board()
    with pytest.raises(ValueError):
        empty_board = board.Board(None)


def test_create_board():
    sides = ['kua', 'smr', 'iod', 'gbj']
    test_board = board.Board(sides)
    assert test_board is not None


def test_board_all_letters():
    sides = ['kua', 'smr', 'iod', 'gbj']
    test_board = board.Board(sides)
    letters = {'k', 'u', 'a', 's', 'm', 'r', 'i', 'o', 'd', 'g', 'b', 'j'}
    assert test_board.get_all_letters == letters


def test_board_valid_next_letters():
    sides = ['kua', 'smr', 'iod', 'gbj']
    test_board = board.Board(sides)

    # all keys in valid next letter map should be the letters of the board
    assert test_board.valid_next_letters.keys() == test_board.get_all_letters

    # a letter from same side should not be in valid next letter map value
    assert 'u' not in test_board.valid_next_letters['k']

    # a valid next letter must exist in one of the boards sides
    assert 'z' not in test_board.valid_next_letters['k']

    # test valid next letter
    assert 's' in test_board.valid_next_letters['k']