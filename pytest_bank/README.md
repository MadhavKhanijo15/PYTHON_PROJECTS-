Reimplemented my bank.py code, restructuring code, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Assuming that the string passed to the value function will not contain any leading spaces.
This program is based on unit testing.
Then, in another file called test_bank.py, implemented three functions that collectively test implementation of value thoroughly.
As to run this code make sure to download pytest library by writing command - pip install pytest.
