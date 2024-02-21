import time
import requests
import json
from board import Board
from dictionary import Dictionary
from letterboxedsolver import LetterBoxedSolver


def get_nyt_metadata():
    r = requests.get('https://www.nytimes.com/puzzles/letter-boxed')
    # Pull metadata from New York Times
    start_string = r.text.index("window.gameData")
    start_parens = start_string + r.text[start_string:].index("{")
    end_string = start_parens + r.text[start_parens:].index(",\"dictionary")
    todays_metadata = json.loads(r.text[start_parens:end_string] + "}")
    return {'sides': todays_metadata['sides'], 'nyt_solution': todays_metadata['ourSolution']}


if __name__ == '__main__':
    # Step 1: Create a dictionary from list of easy words
    # complete: dictionary class method
    start = time.time()
    easy_dictionary = Dictionary("words_easy.txt")
    end = time.time()
    print(f"Creating dictionary took {end - start} seconds")

    # Step 2: Create valid game board
    # complete: create_game_board
    start = time.time()
    todays_metadata = get_nyt_metadata()
    board = Board(todays_metadata['sides'])
    end = time.time()
    print(f"Creating board took {end - start} seconds")

    # What is larger? All possible words from board of a given length?
    # Or the number of words that use only letters from board?
    start = time.time()
    solver = LetterBoxedSolver(board, easy_dictionary, "words_easy.txt")
    end = time.time()
    print(f"Creating solver took {end - start} seconds")

    print(f"Number of words from list that use only letters from board: {len(solver.superset)}")
    print(f"Number of 5 letter words from board: {len(board.generate_strings(5))}")
    print(f"Number of valid words from board: {len(solver.all_valid_words_from_board())}")

    print(f"Two word solutions for board: {solver.get_two_word_solutions()}")
