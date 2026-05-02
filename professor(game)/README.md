This program is based on the toy - Little Professor, a “calculator” that would generate ten different math problems to solve. For instance, if the toy displays 4 + 0 = , one would (hopefully) answer with 4. If the toy displays 4 + 1 = , one would (hopefully) answer with 5. If player answers incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

This program:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program prompts again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits.
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program outputs EEE and prompts the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program outputs the correct answer.
The program ultimately outputs the user’s score: the number of correct answers out of 10.
