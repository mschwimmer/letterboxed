import pytest
import board
import letterboxedsolver


def test_constructor():
    with pytest.raises(TypeError):
        none_params = letterboxedsolver.LetterBoxedSolver(None)
    with pytest.raises(TypeError):
        empty_params = letterboxedsolver.LetterBoxedSolver()
    with pytest.raises(TypeError):
        empty_params = letterboxedsolver.LetterBoxedSolver()


@pytest.fixture
def solver():
    sides = ['kua', 'smr', 'iod', 'gbj']
    solver = letterboxedsolver.LetterBoxedSolver(board.Board(sides), "../words_easy.txt")
    return solver

def test_solver(solver):
    assert solver is not None

