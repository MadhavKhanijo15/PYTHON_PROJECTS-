import pytest
from plates import is_valid

def test_length():
    assert is_valid("OUTATIME")==False
    assert is_valid("H")==False
def test_firsttwoletters():
    assert is_valid("A1")==False
    assert is_valid("1ABC")==False
def test_punctuation():
    assert is_valid("PI3.14")==False
    assert is_valid("Code!")==False
def test_numbers():
    assert is_valid("AAA222") is True
    assert is_valid("AA22A") is False
    assert is_valid("AA065") is False
