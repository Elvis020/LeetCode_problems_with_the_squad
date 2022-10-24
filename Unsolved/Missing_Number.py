def missing_number(nums):
    my_version = list(range(max(nums)+1))
    if len(set(my_version).difference(set(nums))) > 0:
        return set(my_version).difference(set(nums)).pop()
    return max(nums)+1



print(missing_number([0, 1]))
print(missing_number([0, 2]))
print(missing_number([0]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number([3, 0, 1]))
