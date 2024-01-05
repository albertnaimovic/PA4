# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.

from typing import Callable


increase_by_fifteen: Callable[[int], int] = lambda number: number + 15

multiply: Callable[[int, int], int] = lambda x, y: x * y

print(increase_by_fifteen(20))

print(multiply(5, 2))
