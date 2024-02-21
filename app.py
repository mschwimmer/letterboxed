from flask import Flask, render_template
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
    return {'sides': todays_metadata['sides'], 'nyt_solution': todays_metadata['ourSolution']}



@app.route('/')
def index():
    todays_metadata = get_nyt_metadata()
    board = Board(todays_metadata['sides'])
    easy_dictionary = Dictionary("words_easy.txt")
    solver = LetterBoxedSolver(board, easy_dictionary, "words_easy.txt")
    two_word_solutions = solver.get_two_word_solutions()
    print(todays_metadata)

    # if request.method == 'POST':
    #     user_input = request.form['user_word']
    #
    #     flattened_set_of_solution_words = {word for solution in two_word_solutions for word in solution}
    #     isCorrect = user_input in flattened_set_of_solution_words
    #     return render_template('index.html',
    #                        sides=todays_metadata['sides'],
    #                        nyt_solution=todays_metadata['nyt_solution'],
    #                        prog_solutions=two_word_solutions,
    #                            isCorrect=isCorrect,
    #                            user_word=user_input)
    return render_template('index.html',
                           sides=todays_metadata['sides'],
                           nyt_solution=todays_metadata['nyt_solution'],
                           prog_solutions=two_word_solutions)

if __name__ == '__main__':
    app.run(debug=True)