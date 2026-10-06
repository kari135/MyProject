import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import transpose


def test_transpose_square():
    m = [[1, 2], [3, 4]]
    assert transpose(m) == [[1, 3], [2, 4]]


def test_transpose_rectangular():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(m) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_single():
    m = [[7]]
    assert transpose(m) == [[7]]
