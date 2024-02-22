from flask import Flask, request, render_template
import requests
import json
from board import Board
from dictionary import Dictionary
from letterboxedsolver import LetterBoxedSolver

app = Flask(__name__)

def get_nyt_metadata():
    r = requests.get('https://www.nytimes.com/puzzles/letter-boxed')
    # Pull metadata from New York Times
    start_string = r.text.index("window.gameData")
    start_parens = start_string + r.text[start_string:].index("{")
    end_string = start_parens + r.text[start_parens:].index(",\"dictionary")
    todays_metadata = json.loads(r.text[start_parens:end_string] + "}")
    todays_metadata['ourSolution'] = [word.lower() for word in todays_metadata['ourSolution']]
    return {'sides': todays_metadata['sides'], 'nyt_solution': todays_metadata['ourSolution']}

TODAY_METADATA = get_nyt_metadata()
BOARD = Board(TODAY_METADATA['sides'])
EASY_DICTIONARY = Dictionary("words_easy.txt")
SOLVER = LetterBoxedSolver(BOARD, EASY_DICTIONARY, "words_easy.txt")
TWO_WORD_SOLUTIONS = SOLVER.get_two_word_solutions()


@app.route('/')
def index():

    return render_template('index.html',
                           sides=TODAY_METADATA['sides'],
                           nyt_solution=TODAY_METADATA['nyt_solution'],
                           prog_solutions=TWO_WORD_SOLUTIONS)

@app.route('/check_word', methods=['POST'])
def check_word():
    if request.method == 'POST':
        user_input = request.form['user_word'].lower()

        flattened_set_of_solution_words = {word for solution in TWO_WORD_SOLUTIONS for word in solution}
        is_correct = user_input in flattened_set_of_solution_words
        print(user_input)
        print(flattened_set_of_solution_words)
        print(user_input in flattened_set_of_solution_words)
        return render_template('index.html',
                           sides=TODAY_METADATA['sides'],
                           nyt_solution=TODAY_METADATA['nyt_solution'],
                           prog_solutions=TWO_WORD_SOLUTIONS,
                               is_correct=is_correct,
                               user_word=user_input)



if __name__ == '__main__':
    app.run(debug=True)