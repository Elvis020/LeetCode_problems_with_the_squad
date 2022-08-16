import enum
from itertools import accumulate
from math import prod
import operator
from functools import reduce


def productExceptSelf(nums):
    """Given an integer array nums, return an array answer such that answer[i] is 
    equal to the product of all the elements of nums except nums[i].
    
    The product of any prefix or suffix of nums is guaranteed to fit
    in a 32-bit integer.You must write an algorithm that runs 
    in O(n) time and without using the division operation. 
    
    Example
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Args:
        nums (List[int]):
    """
    # Solution 1 - Time Limit Exceeded
    # return [reduce(lambda x,y:x*y,nums[i+1:]+nums[:i]) for i in range(len(nums))]

    # Solution 2 - Time Limit Exceeded
    # return [reduce(operator.mul,nums[index+1:]+nums[:index]) for index,_ in enumerate(nums)]

    # Solution 3 - Timeout
    # d = []
    # for _,element in enumerate(nums):
    #     a = nums.copy()
    #     a.remove(element)
    #     d.append(reduce(operator.mul,a))
    # return d

    # Solution 4 - Timeout
    # pre = [prod(nums[:i]) for i,_ in enumerate(nums)]
    # return [pre[i]*prod(nums[i+1:]) for i,_ in enumerate(nums)]

    # Solution 5
    # pre = [prod(nums[:i]) for i,_ in enumerate(nums)]
    # pos = [prod(nums[i:]) for i,_ in enumerate(nums)]
    # res = list(map(lambda x:x[0]*x[1],zip(pre[:len(pre)-1],pos[1:])))
    # res.append(pre[-1])
    # return res

    # Solution 6 - Timeout
    # arr = [1]*len(nums)
    # pre = [prod(nums[:i]) for i,_ in enumerate(nums)]
    # pos = [prod(nums[i+1:]) for i,_ in enumerate(nums)]
    # for i in range(len(arr)):
    #         arr[i] = pre[i]*pos[i]
    # return arr

    # Solution 7
    arr, left, right = [1] * len(nums), [1] * len(nums), [1] * len(nums)
    for i in range(1,len(nums)):
        left[i] = nums[i - 1] * left[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]
    for i in range(len(arr)):
            arr[i] = left[i]*right[i]
    return arr




















# TODO - write unit test for these examples
# print(productExceptSelf([1, 2, 3, 4]))  # 24,12,8,6
# print(productExceptSelf([-1,1,0,-3,3]))
# print(productExceptSelf([4,5,1,8,2]))