from typing import List

# Has a better time complexity than the one below
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    result = [0] * len(nums1)
    for idx,i in enumerate(nums1):
        found = False
        for idx2,j in enumerate(nums2):
            if found and j>i:
                result[idx] = j
                break
            if j == i:
                found = True
            else:
                result[idx] = -1
    return result

# Has a bad time complexity
def nextGreaterElement_I(nums1: List[int], nums2: List[int]) -> List[int]:
    final_result = []
    for index, element1 in enumerate(nums1):
        for index_2, element2 in enumerate(nums2):
            if index == index_2 and element1 in nums2:
                if len(nums2[nums2.index(element1):]) == 1:
                    final_result.append(-1)
                else:
                    second = 0
                    first = nums2[nums2.index(element1):][0]
                    for i in nums2[nums2.index(element1):][1:]:
                        if i > first:
                            second = i
                            break
                    if second > first:
                        final_result.append(second)
                    if i < first:
                        final_result.append(-1)
    return final_result

print(nextGreaterElement_I([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
print(nextGreaterElement_I([4,1,2], [1,3,4,2]))