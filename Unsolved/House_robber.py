import math


def rob(nums):
    # Method 1 - does not work
    # max_even, max_odd = 0, 0
    # for index, element in enumerate(nums):
    #     if index % 2:
    #         max_odd += element
    #     else:
    #         max_even += element
    # return max_odd if max_odd > max_even else max_even

    # Method 2
    num1, num2 = 0, 0
    for i in nums:
        temp = max(num1 + i, num2)
        num1, num2 = num2, temp
    return num2


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
