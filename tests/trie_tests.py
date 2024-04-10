import pytest
import trie


def test_empty_trie():
    tr = trie.Trie()
    assert tr.search("") is False


def test_add_word():
    tr = trie.Trie()
    tr.insert("Hello")
    assert tr.search("Hello") is True


def test_check_word():
    tr = trie.Trie()
    tr.insert("Hello")
    assert tr.search("Hello") is True
    assert tr.search("Hi") is False
