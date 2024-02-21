class Board:
    """
    This is a Board class. It represents a Letterboxd board.

    It takes 4 sides as parameters.
    It should do the following things:
        1. Create all possible letter combinations of a given length from the board
    """

    def __init__(self, sides):
        if not sides:
            raise ValueError("Missing sides of board!")
        self.sides = sides

    def __str__(self):
        result = ""
        for side in self.sides:
            result += f"Side: {side}"
        return result

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, sides):
        if len(sides) != 4:
            raise ValueError("Need exactly 4 sides!")
        result = []
        for side in sides:
            if len(side) != 3:
                raise ValueError("Each side must contain 3 letters!")
            result.append(list(side.lower()))
        self._sides = result

    @property
    def get_all_letters(self):
        all_letters = set()
        for side in self.sides:
            for letter in side:
                all_letters.add(letter)
        return all_letters

    @property
    def valid_next_letter(self):
        """
        Get valid next letter dictionary.

        :return: A dictionary where keys are a letter on the board,
            and values are all possible next letters on the board.
        """
        valid_letters = {}

        for side in self.sides:
            for letter in side:
                valid_letters[letter] = [letter for letter in self.get_all_letters if letter not in side]
        return valid_letters

    def generate_strings(self, n, last_list_index=-1, current_string=''):
        """
        Generate all possible strings of length n using characters from the lists,
        ensuring no consecutive characters come from the same list.

        :param n: The target length of the strings to generate.
        :param last_list_index: The index of the list from which the last character was taken.
        :param current_string: The current string being built.
        :return: A list of all possible strings of length n.
        """
        if n == 0:
            return [current_string]
        else:
            strings = []
            for i, characters in enumerate(self.sides):
                if i != last_list_index:
                    for letter in characters:
                        strings.extend(self.generate_strings(n-1, i, current_string+letter))
            return strings
