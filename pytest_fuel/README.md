Reimplemented fuel code, restructuring code, wherein:

'convert' expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a positive integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert raised a ValueError. If Y is 0, then convert raises a ZeroDivisionError.
gauge expects an int and returns a str that is:
1.) "E" if that int is less than or equal to 1,
2.) "F" if that int is greater than or equal to 99,
3.) and "Z%" otherwise, wherein Z is that same int.
This program is based on unit testing.
Then, in a file called test_code.py, implemented functions that collectively test implementations of convert and gauge thoroughly.
As to run this code make sure to download pytest library by writing command - pip install pytest.
