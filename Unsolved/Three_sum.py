import itertools


def three_sum_solution(nums):
    # pass

    # Solution 4
    pass

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
print(three_sum_solution([0, 1, 1]))
print(three_sum_solution([0, 0, 0]))