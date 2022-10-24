import itertools


def three_sum_solution(nums):
    # Solution 10: 2 pointer solution
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append(([nums[i], nums[j], nums[k]]))
                while j < k and nums[j] == nums[j + 1]: j += 1
                while j < k and nums[k] == nums[k - 1]: k -= 1
                j += 1
                k -= 1
            elif sum([nums[i], nums[j], nums[k]]) < 0:
                j += 1
            else:
                k -= 1

    return result

    # Solution 9
    # res = []
    # nums.sort()
    # for index, element in enumerate(nums):
    #     if index + 1 < len(nums) and (element + nums[index+1]) * -1 in nums[:index] + nums[index + 1:] :
    #         res.append([element, nums[index + 1], nums[(element + nums[index+1])]])
    # return res

    # Solution 8
    # result = []
    # for index, element in enumerate(nums):
    #     nums = sorted(nums)
    #     if index + 1 < len(nums):
    #         if (element + nums[index + 1]) * -1 in nums \
    #                 and index + 1 != index \
    #                 and nums.index((element + nums[index + 1]) * -1) != index \
    #                 and index + 1 != nums.index((element + nums[index + 1]) * -1) \
    #                 and sorted([(element + nums[index + 1]) * -1, element, nums[index + 1]]) not in result:
    #             result.append(sorted([(element + nums[index + 1]) * -1, element, nums[index + 1]]))
    # return result

    # Solution 7 - 2sum approach TODO: WIP
    # result = []
    # for i in list(itertools.combinations(nums, 3)):
    #     if sum(i) == 0 and sorted(i) not in result:
    #         result.append(list(sorted(i)))
    # return result

    # Solution 6 -> timeout
    # a = []
    # res = [j for j in [list(sorted(i)) for i in list(itertools.combinations(nums, 3))] if sum(j) == 0]
    # for i in res:
    #     if sorted(i) not in a:
    #         a.append(sorted(i))
    # return a

    # Solution 5 -> timeout
    # possible_ans = [list(sorted(i)) for i in list(itertools.combinations(nums, 3))]
    #
    # result_set= []
    # for i in possible_ans:
    #     result = i if sum(i) == 0 else []
    #
    #     if result and result not in result_set:
    #         result_set.append(result)
    # return result_set

    # Solution 3 -> Timeout
    # result = {}
    # for i in list(itertools.combinations(nums, 3)):
    #     if sum(list(i)) not in result:
    #         result[sum(list(i))] = [sorted(list(i))]
    #     elif sorted(list(i)) not in result[sum(list(i))]:
    #             result[sum(list(i))].append(sorted(list(i)))
    # return sum([v for k,v in result.items() if k==0],[])

    # Solution 2 -> Timeout
    # final = []
    # result = [list(i) for i in list(itertools.combinations(nums, 3, )) if sum(i) == 0]
    # for k in result:
    #     if sorted(k) not in final:
    #         final.append(sorted(k))
    # return final

    # Solution 1 -> Wrong
    # for index, element in enumerate(nums):
    #     if len(nums[index:index + 3]) == 3 and sum(nums[index:index + 3]) == 0:
    #         result.append(nums[index:index + 3])
    # return result


print(three_sum_solution([-1, 0, 1, 2, -1, -4]))
print()
# print(three_sum_solution([0, 1, 1]))
# print(three_sum_solution([0, 0, 0]))
# print(three_sum_solution([1, -1, -1, 0]))
# print(three_sum_solution([3, -2, 1, 0]))
print(three_sum_solution([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
print(three_sum_solution([-8, -7, 5, 2]))
print(three_sum_solution([0, 0, 0, 0]))
# Expected: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

# Output -> [[1,-1,0],[1,-1,0]]
# Expected -> [[-1,0,1]]