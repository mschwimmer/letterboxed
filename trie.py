class TrieNode:
    def __init__(self):
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.terminal = True

    def search(self, word):
        """
        Returns True if the word is in the Trie, False otherwise.
        """
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.terminal


if __name__ == "__main__":
    tr = Trie()
    tr.insert("Hello")

    print(tr)
    print(tr.search("Hello"))
