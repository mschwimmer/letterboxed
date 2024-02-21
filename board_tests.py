import pytest
import board


def test_empty_board_fails():
    with pytest.raises(TypeError):
        empty_board = board.Board()
    with pytest.raises(ValueError):
        empty_board = board.Board(None)


def test_create_board():
    sides = [['k', 'u', 'a'],
             ['s', 'm', 'r'],
             ['i', 'o', 'd'],
             ['g', 'b', 'j']]
    test_board = board.Board(sides)
    assert test_board is not None


def test_board_all_letters():
    sides = [['k', 'u', 'a'],
             ['s', 'm', 'r'],
             ['i', 'o', 'd'],
             ['g', 'b', 'j']]
    test_board = board.Board(sides)
    letters = {'k', 'u', 'a', 's', 'm', 'r', 'i', 'o', 'd', 'g', 'b', 'j'}
    assert test_board.get_all_letters == letters
