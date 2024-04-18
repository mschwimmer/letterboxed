import collections


class LetterBoxedSolver:
    def __init__(self, board, file):
        if not board:
            raise ValueError("Missing Board!")
        self.board = board
        if not file:
            raise ValueError("Missing file name")
        self.all_valid_words = self.load_valid_words_from_file(file)
        self.words_from_first_letter = self.get_words_from_first_letter_dict()

    def load_valid_words_from_file(self, file):
        """
        Load all words from file. Filter out invalid words.
        :param str file:
        :return: List of words that contain characters from board
        :rtype List
        """
        superset = []
        with (open(file, 'r') as file):
            for word in file:
                word = word.strip().lower()
                if set(word).issubset(self.board.get_all_letters) and len(word) > 1 and self.valid(word):
                    superset.append(word)

        return superset


    def valid(self, word):
        """
        A word is valid as long as the next letter is not in the same side on the board
        :param str word: a word that may or may not be valid for the board
        :return: True if word is valid
        :rtype bool
        """
        for i in range(len(word) - 1):
            if i == len(word) - 1:
                return True
            if word[i+1] not in self.board.valid_next_letters[word[i]]:
                return False
        return True


    def valid_solution(self, words):
        """
        A solution is valid if the len(set(words)) == 12 and
        word[0] == prev_word[-1]
        :param list words: an ordered list of words for a letterboxed solution
        :return: True if given words create a valid Letterboxed solution to the board
        :rtype bool
        """
        if len(set(''.join(words))) != 12:
            return False
        last_letter = words[0][0]
        for word in words:
            if word[0] != last_letter or not self.valid(word):
                return False
            last_letter = word[-1]
        return True


    def get_words_from_first_letter_dict(self):
        """
        A dictionary where keys are letters and values are list of valid words which start with that letter
        :return: A dictionary {'letter': [words that start with letter]}
        :rtype dict
        """
        result = collections.defaultdict(list)

        for word in self.all_valid_words:
            result[word[0]].append(word)

        return result


    def get_two_word_solutions(self):
        """
        Iterate through every valid word. Then check all other valid words that start with last letter of first word.
        If both words are a valid letterboxed solution, append to result list.
        :return: List of 2 word solutions for the board
        :rtype List
        """
        word_bank = self.all_valid_words
        solutions = []
        for word in word_bank:
            last_letter = word[-1]
            possible_next_words = self.words_from_first_letter[last_letter]
            for next_word in possible_next_words:
                if self.valid_solution([word, next_word]):
                    solutions.append([word, next_word])
        return solutions


