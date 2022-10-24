import heapq
from typing import List


class KthLargest:
    # The solution to this problem can be effectively done using a heap(min variation)
    def __init__(self,k:int,nums:List[int]):
         self.heap = nums
         self.k = k
        #  This converts the list into a heap
         heapq.heapify(self.heap)

    
    def add(self,val:int) -> int:
        # This adds val to the heap and makes sure its sorted
        heapq.heappush(self.heap,val)

        # Popping from a heap always pops the smallest element among the K-number of elements
        return self.heap[0]

l = KthLargest(3, [4, 5, 8, 2])
# l.add(3)
# l.add(5)
# l.add(10)
# l.add(9)
# l.add(4)


# l = KthLargest(1,[])
# l.add(-3)
# l.add(-2)
# l.add(-4)
# l.add(0)
# l.add(4)