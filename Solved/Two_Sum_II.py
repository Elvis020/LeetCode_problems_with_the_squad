def twoSumII(nums,target):
    res = set()
    for index, element in enumerate(nums):
        ans = target - element
        if ans in res:
            return list(map(lambda x: x + 1, [nums.index(ans), index]))
        res.add(element)

# print(twoSumII([2, 7, 11, 15], 9))
# print(twoSumII([-1,0], -1))
# print(twoSumII([2,3,4], 6))





















# TODO - write unit test for these examples
# print(twoSumII([2, 7, 11, 15], 9))
# print(twoSumII([-1,0], -1))
# print(twoSumII([2,3,4], 6))