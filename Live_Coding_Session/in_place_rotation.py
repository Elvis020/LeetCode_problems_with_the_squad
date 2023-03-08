from typing import List


# Iteration - 20.89%
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        last_element = nums.pop()
        nums.insert(0, last_element)


# Iteration 2 - Better version(93.21%)
def rotate_II(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)  # very helpful tip
    nums[:] = nums[-k:] + nums[:-k]


print(rotate_II(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(rotate_II(nums=[1, 2], k=3))