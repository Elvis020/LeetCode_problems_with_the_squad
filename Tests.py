import pytest

from Solved.NbyNProblem import solution
from Solved.ContainsDups import contains_duplicate
from Solved.TopKElement import solution_2
from Solved.Valid_parenthesis import is_valid
from Solved.Letter_Combination import letter_combination


@pytest.mark.parametrize(
    'arg,result', [
        ([[2, 2, 3],
          [5, 4, 6],
          [7, 8, 1]], "17 is a prime"),
        ([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]], "68 is not a prime"),
        ([[9, 3, 2, 1],
          [8, 4, 2, 2],
          [2, 2, 7, 1],
          [3, 3, 0, 3]], "31 is a prime"),
        ([[1, 2],
          [3, 4]], "10 is not a prime"),
        (4, "4 is not a prime"),
        (7, "7 is a prime"),
    ]
)
def test_is_prime_problem(arg, result):
    assert solution(arg) == result


@pytest.mark.parametrize(
    'arg1,arg2,result', [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([-1, -1], 1, [-1]),
        ([3, 0, 1, 0], 1, [0]),
        ([5, 3, 1, 1, 1, 3, 73, 1], 1, [1]),
    ]
)
def test_top_K_element(arg1, arg2, result):
    # assert solution(arg1, arg2) == result
    assert solution_2(arg1, arg2) == result


@pytest.mark.parametrize(
    'arg,result', [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
)
def test_contains_duplicate(arg, result):
    assert contains_duplicate(arg) == result


@pytest.mark.parametrize(
    'arg,result', [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("{[]}", True),
        ("([)]", False),
        ("]", False),
        ("){", False),
    ]
)
def test_is_valid(arg, result):
    assert is_valid(arg) == result


@pytest.mark.parametrize(
    'nums,result', [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ['a', 'b', 'c']),
        ("", []),
        ("234",
         ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei',
          'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']),
    ]
)
def test_letter_combination(nums, result):
    assert letter_combination(nums) == result