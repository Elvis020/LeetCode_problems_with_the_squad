def climbStairs(stairs):
    first,second = 0,1
    # The ways of climbing stairs is a fibonacci sequence
    for i in range(stairs+1):
        stairs_list = first+second
        second = first
        first = stairs_list
    return stairs_list


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))  # [1,2,3,4] 1,1,1,1 -> 2,2 ->  1,1,2,2 -> 2,1,1 -> 1,1,2
print(climbStairs(5))  # [1,2,3,4] 1,1,1,1 -> 2,2 ->  1,1,2,2 -> 2,1,1 -> 1,1,2
