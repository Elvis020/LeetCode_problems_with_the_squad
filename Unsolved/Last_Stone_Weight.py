from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) > 1:
        stones = sorted(stones)
        stones.append(stones.pop() - stones.pop())
    return stones[0]


print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(lastStoneWeight([1]))
print(lastStoneWeight([1, 3]))
print(lastStoneWeight([3, 7, 8]))
