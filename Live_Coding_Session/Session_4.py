from typing import List


# def moveZeros(nums: List[int]):
#     newNums = []
#     for i, element in enumerate(nums):
#         if element != 0:
#             newNums.append(element)
#     for _ in range(nums.count(0)):
#         newNums.append(0)
#     return newNums

def moveZeros(nums: List[int]):
    if not len(nums):
        return nums
    i, keepNumsCount = 0, 0
    while keepNumsCount < len(nums):
        if nums[i] == 0:
            nums.insert(len(nums) - 1, nums.pop(i)) # swap is bad
        elif nums[i] != 0:
            i += 1
        keepNumsCount += 1
    return nums


print(moveZeros([0, 1, 0, 3, 12]))
print(moveZeros([0, 0, 1]))
print(moveZeros([0]))
