from trie import Trie


class Dictionary(Trie):
    """
    This is a Dictionary. It extends the Trie class.
    It takes a board and a word list as inputs.
    It inserts all words from word list that contain letters from the given board.
    Thus, it is used to efficiently check if a word
    """

    def __init__(self, board, file=None):
        super().__init__()
        self.board = board
        if file is not None:
            self.ingest_words(file)

    def ingest_words(self, file):
        """
        Adds words to Dictionary Trie.
        Only add a word to the dictionary if all letters are part of board
        """
        with open(file, 'r') as f:
            lines = f.readlines()
            for word in lines:
                if set(word).issubset(self.board.get_all_letters) and len(word) > 1:
                    self.insert(word.lower().strip())

