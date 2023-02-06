# Given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency of any one
# of its elements.
from collections import Counter


# Your task is to find the smallest possible length of a (contiguous)
# subarray of nums, that has the same degree as nums.

# Input: nums = [1,2,2,3,1]
# Output: 2

# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.


def findShortestSubArray(arr):
    if set(arr) == arr: return 1


    dict_arr = Counter(arr)
    selected = [i for i,j in dict_arr.items() if j == max(dict_arr.values())]

    subArrs,new_sub = [],[]
    i,j = 0,len(arr)-1


    while True:
        if i <= len(arr)-1:
            print(arr[i:])
            i += 1


        elif j > 0:
            print(arr[:j])
            j -= 1

    # for index,element in enumerate(arr):
    #     for l in selected:
    #         if arr[index:j+1].count(l) >= max(dict_arr.values()):
    #             subArrs.append(arr[index:j+1])
    #             i += 1
    #             j -= 1
    #
    # for index,element in enumerate(arr):
    #     for l in selected:
    #         if arr[index:j+1].count(l) >= max(dict_arr.values()):
    #             subArrs.append(arr[index:j+1])
    #             j -= 1
    #
    # for i in subArrs:
    #     for j in selected:
    #         if i.count(j) >= max(dict_arr.values()):
    #             new_sub.append(i)




    # print(max_frequency)
    # print(selected)
    # print(subArrs)
    # print('MAXY',max(dict_arr.values()))
    # print(new_sub)
    # # print(subArrs,selected,max_frequency)
    # return sorted(new_sub,key=lambda x:len(x))[0]




# nums = [1,2,2,3,1]
# nums_2 = [1, 2, 2, 3, 1, 4, 2]
nums_3 = [1,1,2,2,2,1]
# print(findShortestSubArray(nums))
# print(findShortestSubArray(nums_2))
print(findShortestSubArray(nums_3))