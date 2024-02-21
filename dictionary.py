from trie import Trie


class Dictionary(Trie):

    def __init__(self, board, file=None):
        super().__init__()
        self.board = board
        if file is not None:
            self.ingest_words(file)

    def ingest_words(self, file):
        """
        Only add a word to the dictionary if the letters are part of the board
        """
        with open(file, 'r') as f:
            lines = f.readlines()
            for word in lines:
                if set(word).issubset(self.board.get_all_letters) and len(word) > 1:
                    self.insert(word.lower().strip())

