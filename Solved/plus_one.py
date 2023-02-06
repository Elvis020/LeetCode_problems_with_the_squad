def plusOne(nums):
    conv = "".join([str(i) for i in nums])
    return list(map(int,list(str(eval(conv+"+1")))))


print(plusOne([1, 2, 3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))