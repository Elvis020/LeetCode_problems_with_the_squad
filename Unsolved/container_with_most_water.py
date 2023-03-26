from typing import List


def maxArea(height: List[int]):
    lst = [(i, j) for i, j in enumerate(height, start=0)]
    return lst


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
