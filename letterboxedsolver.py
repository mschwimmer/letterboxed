import collections


class LetterBoxedSolver:
    def __init__(self, board, dictionary, file):
        self.board = board
        self.dictionary = dictionary
        self.superset = self.load_word_superset_from_file(file)
        self.all_valid_words = self.all_valid_words_from_board()
        self.words_from_first_letter = self.get_words_from_first_letter_dict()

    def load_word_superset_from_file(self, file):
        """
        Load and filter all words to only words that use letters in the board.
        This is a superset of words, and each word is not necessarily a valid word for our board.
        :param file:
        :return:
        """
        superset = []
        with open(file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                if set(word).issubset(self.board.get_all_letters) and len(word) > 1:
                    superset.append(word)

        return superset

    def all_valid_words_from_board(self):
        valid_words = []
        for word in self.superset:
            if self.valid(word):
                valid_words.append(word)

        return valid_words

    def valid(self, word):
        """
        A word is valid as long as the next letter is not in the same side on the board
        """
        for i in range(len(word) - 1):
            if i == len(word) - 1:
                return True
            if word[i+1] not in self.board.valid_next_letter[word[i]]:
                return False
        return True

    def valid_solution(self, words):
        """
        A solution is valid if the len(set(words)) == 9 and
        word[0] == prev_word[-1]
        """
        if len(set(''.join(words))) != 12:
            return False
        last_letter = words[0][-1]
        for i in range(1, len(words) - 1):
            if words[i][0] != last_letter:
                return False
            last_letter = words[i][-1]
        return True

    def get_two_word_solutions(self):
        word_bank = self.all_valid_words
        solutions = []
        for word in word_bank:
            last_letter = word[-1]
            possible_next_words = self.words_from_first_letter[last_letter]
            for next_word in possible_next_words:
                if self.valid_solution([word, next_word]):
                    solutions.append([word, next_word])
        return solutions

    def get_words_from_first_letter_dict(self):
        result = collections.defaultdict(list)

        for word in self.all_valid_words:
            result[word[0]].append(word)

        return result
