"""
Consider an N x N matrix of integers. As part of this problem we’d like you to calculate the sum of the elements in the given matrix’s diagonals and determine whether the result is a prime number. The output should be a string in the following format “<sum> is a prime” or “<sum> is not a prime”.

Remember that a prime number is a whole number greater than 1 whose only factors are 1 and itself.

Note that if N is an odd number, the centre element should only be added once.


Examples:

Input 1:
2 2 3
5 4 6
7 8 1

Output 1: 17 is a prime


Input 2:
9 3 2 1
8 4 2 2
2 2 7 1
3 3 0 3

Output 2: 31 is a prime


Input 3:
1 2
3 4

Output 3: 10 is not a prime


Input 4:
4

Output 4: 4 is not a prime
"""

# TODO: rewrite the check if prime for very large numbers
import math


def solution(matrix):
    def check_if_prime(number):
        is_prime = (list(number % i for i in range(1, int(math.sqrt(number)+1)))).count(0) == 1
        return f"{number} is a prime" if is_prime else f"{number} is not a prime"

    # matrix is not a number
    if type(matrix) is not list:
        return check_if_prime(matrix)
    else:
        # Extract diagonals
        n = len(matrix[0])
        right = [matrix[i][i] for i in range(n)]
        left = [matrix[i][(n - 1) - i] for i in range(n) if i != (n - 1) - i]
        result = sum(right) + sum(left)

        # Check if its prime
        return check_if_prime(result)