import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("Google") == "Ggl"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
